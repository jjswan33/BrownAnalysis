#ifndef BrownAnalysis_RecoTools_CompositePtrCandidateT1T2MEtProducer_h
#define BrownAnalysis_RecoTools_CompositePtrCandidateT1T2MEtProducer_h

/** \class CompositePtrCandidateT1T2MEtProducer
 *
 * Produce combinations of leptonic and hadronic decay products 
 * of a pair of tau leptons plus missing transverse momentum 
 * (representing the undetected momentum carried away by the neutrinos 
 *  produced in the two tau decays) 
 * 
 * \authors Colin Bernet,
 *          Michal Bluj,
 *          Christian Veelken
 *
 * \version $Revision: 1.9 $
 *
 * $Id: CompositePtrCandidateT1T2MEtProducer.h,v 1.9 2013/06/20 16:35:01 ojalvo Exp $
 *
 */

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/View.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "BrownAnalysis/RecoTools/interface/FetchCollection.h"

#include "BrownAnalysis/DataFormats/interface/CompositePtrCandidateT1T2MEt.h"
#include "BrownAnalysis/DataFormats/interface/CompositePtrCandidateT1T2MEtFwd.h"

#include "BrownAnalysis/RecoTools/interface/CompositePtrCandidateT1T2MEtAlgorithm.h"
#include "BrownAnalysis/RecoTools/interface/CompositePtrCandidateT1T2MEtVertexAlgorithm.h"
#include "BrownAnalysis/RecoTools/interface/METCalibrator.h"

#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include <string>

bool IsRealData=false; 

template<typename T1, typename T2>
class CompositePtrCandidateT1T2MEtProducer : public edm::EDProducer 
{
  typedef edm::Ptr<T1> T1Ptr;
  typedef edm::Ptr<T2> T2Ptr;
  typedef std::vector<edm::Ptr<pat::Jet> > JetPtrVector;
  typedef std::vector<CompositePtrCandidateT1T2MEt<T1,T2> > CompositePtrCandidateCollection;
  
 public:

  explicit CompositePtrCandidateT1T2MEtProducer(const edm::ParameterSet& cfg)
    : algorithm_(cfg), cfgError_(0)
  {
    useLeadingTausOnly_ = cfg.getParameter<bool>("useLeadingTausOnly");
    srcLeg1_ = cfg.getParameter<edm::InputTag>("srcLeg1");
    srcLeg2_ = cfg.getParameter<edm::InputTag>("srcLeg2");
    srcJets_ = cfg.getParameter<edm::InputTag>("srcJets");
    dRmin12_ = cfg.getParameter<double>("dRmin12");
    srcMET_ = ( cfg.exists("srcMET") ) ? cfg.getParameter<edm::InputTag>("srcMET") : edm::InputTag();
    srcTaus_ =  cfg.getParameter<edm::InputTag>("srcTaus");//( cfg.exists("srcTaus") ) ? cfg.getParameter<edm::InputTag>("srcTaus") : edm::InputTag();
    srcGenParticles_ = ( cfg.exists("srcGenParticles") ) ? cfg.getParameter<edm::InputTag>("srcGenParticles") : edm::InputTag();
    recoMode_ = cfg.getParameter<std::string>("recoMode");
    verbosity_ = cfg.getUntrackedParameter<int>("verbosity", 0);
    minPt_ = cfg.getUntrackedParameter<double>("minJetPt", 20.0);


    //met calibration

    edm::ParameterSet calibrationSet =cfg.getParameter<edm::ParameterSet>("metCalibration"); 
    calibrator_ = new METCalibrator(calibrationSet);
    algorithm_.setMETCalibrator(calibrator_);
				    


//--- check that InputTag for MET collection has been defined,
//    in case it is needed for the reconstruction mode 
//    specified in the configuration parameter set
    if ( srcMET_.label() == "" && recoMode_ != "" ) {
      edm::LogError ("CompositePtrCandidateT1T2MEtProducer") << " Configuration Parameter srcMET undefined," 
							     << " needed for recoMode = " << recoMode_ << " !!";
      cfgError_ = 1;
    }
    
    produces<CompositePtrCandidateCollection>("");
  }

  ~CompositePtrCandidateT1T2MEtProducer() {}

  void produce(edm::Event& evt, const edm::EventSetup& es)
  {
    //Instantiate the vertex Algorithm
    //CompositePtrCandidateT1T2MEtVertexAlgorithm<T1,T2> vAlgo(evt,es);

//--- print-out an error message and add an empty collection to the event 
//    in case of erroneous configuration parameters

    if(evt.isRealData()){
      IsRealData=true;
    }

    if ( cfgError_ ) {
      edm::LogError ("produce") << " Error in Configuration ParameterSet" 
				<< " --> CompositePtrCandidateT1T2MEt collection will NOT be produced !!";
      std::auto_ptr<CompositePtrCandidateCollection> emptyCompositePtrCandidateCollection(new CompositePtrCandidateCollection());
      evt.put(emptyCompositePtrCandidateCollection);
      return;
    }

    typedef edm::View<T1> T1View;
    edm::Handle<T1View> leg1Collection;
    pf::fetchCollection(leg1Collection, srcLeg1_, evt);

    edm::Handle<edm::View<pat::Jet> > jetCollection;
    pf::fetchCollection(jetCollection, srcJets_, evt);

    typedef edm::View<T2> T2View;
    edm::Handle<T2View> leg2Collection;
    pf::fetchCollection(leg2Collection, srcLeg2_, evt);

    const std::vector<pat::Tau>* tauPtr = 0;
    if ( srcTaus_.label() != "" ) {
      edm::Handle<std::vector<pat::Tau> > tauCollection;
      if(evt.getByLabel(srcTaus_,tauCollection))
	tauPtr = tauCollection.product();
	//pf::fetchCollection(tauCollection, srcTaus_, evt);

      //std::cout<< "Got Taus: " << tauCollection->size()<<endl;
    }
  
    reco::CandidatePtr metPtr;
    if ( srcMET_.label() != "" ) {
      edm::Handle<reco::CandidateView> metCollection;
      pf::fetchCollection(metCollection, srcMET_, evt);
      
//--- check that there is exactly one MET object in the event
//    (missing transverse momentum is an **event level** quantity)
      if ( metCollection->size() == 1 ) {
	metPtr = metCollection->ptrAt(0);
      } else {
	edm::LogError ("produce") << " Found " << metCollection->size() << " MET objects in collection = " << srcMET_ << ","
				  << " --> CompositePtrCandidateT1T2MEt collection will NOT be produced !!";
	std::auto_ptr<CompositePtrCandidateCollection> emptyCompositePtrCandidateCollection(new CompositePtrCandidateCollection());
	evt.put(emptyCompositePtrCandidateCollection);
	return;
      }
    }

    const reco::GenParticleCollection* genParticles = 0;
    if ( srcGenParticles_.label() != "" ) {
      edm::Handle<reco::GenParticleCollection> genParticleCollection;
      if(evt.getByLabel(srcGenParticles_,genParticleCollection))
	genParticles = genParticleCollection.product();
    }


    JetPtrVector pfJets;
    for(unsigned int i=0;i<jetCollection->size();++i)
      if(jetCollection->at(i).pt()>minPt_)
	pfJets.push_back(jetCollection->ptrAt(i));
      


//--- check if only one combination of tau decay products 
//    (the combination of highest Pt object in leg1 collection + highest Pt object in leg2 collection)
//    shall be produced, or all possible combinations of leg1 and leg2 objects
    std::auto_ptr<CompositePtrCandidateCollection> compositePtrCandidateCollection(new CompositePtrCandidateCollection());
    if ( useLeadingTausOnly_ ) {

//--- find highest Pt particles in leg1 and leg2 collections
      int idxLeadingLeg1 = -1;
      double leg1PtMax = 0.;
      for ( unsigned idxLeg1 = 0, numLeg1 = leg1Collection->size(); 
	    idxLeg1 < numLeg1; ++idxLeg1 ) {
	T1Ptr leg1Ptr = leg1Collection->ptrAt(idxLeg1);
	if ( idxLeadingLeg1 == -1 || leg1Ptr->pt() > leg1PtMax ) {
	  idxLeadingLeg1 = idxLeg1;
	leg1PtMax = leg1Ptr->pt();
	}
      }
      
      int idxLeadingLeg2 = -1;
      double leg2PtMax = 0.;
      for ( unsigned idxLeg2 = 0, numLeg2 = leg2Collection->size(); 
	    idxLeg2 < numLeg2; ++idxLeg2 ) {
	T2Ptr leg2Ptr = leg2Collection->ptrAt(idxLeg2);

//--- do not create CompositePtrCandidateT1T2MEt object 
//    for combination of particle with itself
	if ( idxLeadingLeg1 != -1 ) {
	  T1Ptr leadingLeg1Ptr = leg1Collection->ptrAt(idxLeadingLeg1);
	  double dR = reco::deltaR(leadingLeg1Ptr->p4(), leg2Ptr->p4());
	  if ( dR < dRmin12_ ) continue;
	}
	
	if ( idxLeadingLeg2 == -1 || leg2Ptr->pt() > leg2PtMax ) {
	  idxLeadingLeg2 = idxLeg2;
	  leg2PtMax = leg2Ptr->pt();
	}
      }
      
      if ( idxLeadingLeg1 != -1 &&
	   idxLeadingLeg2 != -1 ) {
	T1Ptr leadingLeg1Ptr = leg1Collection->ptrAt(idxLeadingLeg1);
	T2Ptr leadingLeg2Ptr = leg2Collection->ptrAt(idxLeadingLeg2);
	
	CompositePtrCandidateT1T2MEt<T1,T2> compositePtrCandidate = 
	  algorithm_.buildCompositePtrCandidate(leadingLeg1Ptr, leadingLeg2Ptr,pfJets, metPtr, tauPtr, IsRealData, genParticles);
	compositePtrCandidateCollection->push_back(compositePtrCandidate);
      } else {
	if ( verbosity_ >= 1 ) {
	  edm::LogInfo ("produce") << " Found no combination of particles in Collections" 
				   << " leg1 = " << srcLeg1_ << " and leg2 = " << srcLeg2_ << ".";
	}
      }
    } else {
//--- check if the same collection is used on both legs;
//    if so, skip diTau(j,i), j > i combination in order to avoid two diTau objects being produced
//    for combinations (i,j) and (j,i) of the same pair of particles in leg1 and leg2 collections
      bool sameCollection = (leg1Collection.id () == leg2Collection.id());
   
      for ( unsigned idxLeg1 = 0, numLeg1 = leg1Collection->size(); 
	    idxLeg1 < numLeg1; ++idxLeg1 ) {
	T1Ptr leg1Ptr = leg1Collection->ptrAt(idxLeg1);
	
	unsigned idxLeg2_first = ( sameCollection ) ? (idxLeg1 + 1) : 0;
	for ( unsigned idxLeg2 = idxLeg2_first, numLeg2 = leg2Collection->size(); 
	      idxLeg2 < numLeg2; ++idxLeg2 ) {
	  T2Ptr leg2Ptr = leg2Collection->ptrAt(idxLeg2);

//--- do not create CompositePtrCandidateT1T2MEt object 
//    for combination of particle with itself
	  double dR = reco::deltaR(leg1Ptr->p4(), leg2Ptr->p4());
	  if ( dR < dRmin12_ ) continue;
	  
	  CompositePtrCandidateT1T2MEt<T1,T2> compositePtrCandidate = 
	    algorithm_.buildCompositePtrCandidate(leg1Ptr, leg2Ptr, pfJets, metPtr, tauPtr, IsRealData, genParticles);

	  //vAlgo.calculateVertexVariables(compositePtrCandidate);
	  compositePtrCandidateCollection->push_back(compositePtrCandidate);
	}
      }
    }

//--- add the collection of reconstructed CompositePtrCandidateT1T2MEts to the event
    evt.put(compositePtrCandidateCollection);
    }
  
 private:

  CompositePtrCandidateT1T2MEtAlgorithm<T1,T2> algorithm_;
  
  bool useLeadingTausOnly_;
  edm::InputTag srcLeg1_;
  edm::InputTag srcLeg2_;
  edm::InputTag srcJets_;
  double dRmin12_;
  edm::InputTag srcMET_;
  edm::InputTag srcTaus_;
  edm::InputTag srcGenParticles_;
  std::string recoMode_;
  int verbosity_;
  double minPt_;
  int cfgError_;


  METCalibrator *calibrator_;

};

#endif

