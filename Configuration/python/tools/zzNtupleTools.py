from UWAnalysis.Configuration.tools.analysisTools import TriggerPaths
import FWCore.ParameterSet.Config as cms

def zzCommon(src,pluginType):
	sharedV = cms.VPSet(
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("mass"),
				method     = cms.string("mass()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("charge"),
				method     = cms.string("charge()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("z1Mass"),
				method     = cms.string("leg1.mass()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("z2Mass"),
				method     = cms.string("leg2.mass()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("z1Pt"),
				method     = cms.string("leg1.pt()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("z2Mass"),
				method     = cms.string("leg2.pt()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("z1Eta"),
				method     = cms.string("leg1.eta()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("z2Eta"),
				method     = cms.string("leg2.eta()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("z1Phi"),
				method     = cms.string("leg1.phi()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("z2Phi"),
				method     = cms.string("leg2.phi()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("met"),
				method     = cms.string("met.pt()"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("mt"),
				method     = cms.string("mt12MET"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("mt1"),
				method     = cms.string("mt1MET"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("mt1_12"),
				method     = cms.string("leg1.mt12MET"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string("mt1_1"),
				method     = cms.string("leg1.mt1MET"),
				leadingOnly=cms.untracked.bool(True)
				),
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag        = cms.string("mt1_2"),
					method     = cms.string("leg1.mt2MET"),
					leadingOnly=cms.untracked.bool(True)
					),
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag        = cms.string("mt2"),
					method     = cms.string("mt2MET"),
					leadingOnly=cms.untracked.bool(True)
					),
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag        = cms.string("mt2_12"),
					method     = cms.string("leg2.mt12MET"),
					leadingOnly=cms.untracked.bool(True)
					),
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag        = cms.string("mt2_1"),
					method     = cms.string("leg2.mt1MET"),
					leadingOnly=cms.untracked.bool(True)
					),
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag        = cms.string("mt2_2"),
					method     = cms.string("leg2.mt2MET"),
					leadingOnly=cms.untracked.bool(True)
					),
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag		 = cms.string("dZ12"),
					method     = cms.string('leg1.dz'),
					leadingOnly= cms.untracked.bool(True)
					),
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag		 = cms.string("dZ13"),
					method     = cms.string('abs(leg1.z1-leg2.z1)'),
					leadingOnly= cms.untracked.bool(True)
					),
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag		 = cms.string("dZ14"),
					method     = cms.string('abs(leg1.z1-leg2.z2)'),
					leadingOnly= cms.untracked.bool(True)
					),	
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag		 = cms.string("z1l1Z"),
					method     = cms.string('leg1.z1'),
					leadingOnly= cms.untracked.bool(True)
					),	
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag		 = cms.string("z1l2Z"),
					method     = cms.string('leg1.z2'),
					leadingOnly= cms.untracked.bool(True)
					),	
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag		 = cms.string("z2l1Z"),
					method     = cms.string('leg2.z1'),
					leadingOnly= cms.untracked.bool(True)
					),	
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag		 = cms.string("z2l2Z"),
					method     = cms.string('leg2.z2'),
					leadingOnly= cms.untracked.bool(True)
					),	
			cms.PSet(
					pluginType = cms.string(pluginType),
					src        = cms.InputTag(src),
					tag		 = cms.string("rho"),
					method     = cms.string('leg1.leg1.userFloat("rho")'),
					leadingOnly= cms.untracked.bool(True)
					),	
			)
	return sharedV

def muCommon(src,legName,legMethod,pluginType):
	sharedV = cms.VPSet(
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"Pt"),
			method     = cms.string(legMethod+"pt"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"Eta"),
			method     = cms.string(legMethod+"eta"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"Phi"),
			method     = cms.string(legMethod+"phi"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"ValidMuonHits1"),
			method     = cms.string(legMethod+"globalTrack().hitPattern().numberOfValidMuonHits()"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"numMatches"),
			method     = cms.string(legMethod+"numberOfMatches()"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"ValidHits"),
			method     = cms.string(legMethod+"numberOfValidHits()"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"NormChiSq"),
			method     = cms.string(legMethod+"normChi2()"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"StdIsoEcaldR03"),
			method     = cms.string(legMethod+"isolationR03().emEt"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"StdIsoEcal"),
			method     = cms.string(legMethod+"userIso(1)"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"StdIsoHcaldR03"),
			method     = cms.string(legMethod+"isolationR03().hadEt"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"StdIsoHcal"),
			method     = cms.string(legMethod+"userIso(2)"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"StdIsoTk"),
			method     = cms.string(legMethod+"userIso(3)"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"RelPFIsoDB"),
			method     = cms.string("("+legMethod+"chargedHadronIso+max("+legMethod+"photonIso()+"+legMethod+"neutralHadronIso()-0.5*"+legMethod+"userIso(0),0.0))/"+legMethod+"pt()"),
			leadingOnly=cms.untracked.bool(True)
		),
	  	cms.PSet(
		  	pluginType = cms.string(pluginType),
		  	src        = cms.InputTag(src),
		  	tag        = cms.string(legName+"RelPfIsoRho"),
		  	method     = cms.string("("+legMethod+"chargedHadronIso()+max("+legMethod+"photonIso()+"+legMethod+"neutralHadronIso()-"+legMethod+"userFloat('rho')*3.14*0.4*0.4,0.0))/"+legMethod+"pt()"),
		  	leadingOnly=cms.untracked.bool(True)
	  	),
	  	cms.PSet(
		  	pluginType = cms.string(pluginType),
		  	src        = cms.InputTag(src),
		  	tag        = cms.string(legName+"dB"),
		  	method     = cms.string(legMethod+"userIso(0)"),
		  	leadingOnly=cms.untracked.bool(True)
	  	)
		)
	return sharedV

def tauCommon(src,legName,legMethod,pluginType):
	sharedV = cms.VPSet(
		cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string(legName+"Eta"),
				method     = cms.string(legMethod+"eta"),
				leadingOnly=cms.untracked.bool(True)
				),
		cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string(legName+"Pt"),
				method     = cms.string(legMethod+"pt"),
				leadingOnly=cms.untracked.bool(True)
				),
		cms.PSet(
				pluginType = cms.string(pluginType),
				src        = cms.InputTag(src),
				tag        = cms.string(legName+"JetPt"),
				method     = cms.string(legMethod+"pfJetRef.pt"),
				leadingOnly=cms.untracked.bool(True)
				),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"Prongs"),
			method     = cms.string(legMethod+"signalPFChargedHadrCands.size()"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"Gammas"),
			method     = cms.string(legMethod+"signalPFGammaCands.size()"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"Mass"),
			method     = cms.string(legMethod+"mass()"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"VLooseIso"),
			method     = cms.string(legMethod+"tauID('byVLooseIsolation')"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"LooseIso"),
			method     = cms.string(legMethod+"tauID('byLooseIsolation')"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"MediumIso"),
			method     = cms.string(legMethod+"tauID('byMediumIsolation')"),
			leadingOnly=cms.untracked.bool(True)
		),
	    cms.PSet(
	    	pluginType  = cms.string(pluginType),
	    	src		    = cms.InputTag(src),
	    	tag			= cms.string(legName+"QIso"),
	    	method		= cms.string(legMethod+"isolationPFChargedHadrCandsPtSum()"),
	    	leadingOnly	= cms.untracked.bool(True)
	    ),
	    cms.PSet(
	    	pluginType  = cms.string(pluginType),
	    	src		    = cms.InputTag(src),
	    	tag			= cms.string(legName+"NIso"),
	    	method		= cms.string(legMethod+"isolationPFGammaCandsEtSum()"),
	    	leadingOnly	= cms.untracked.bool(True)
	    ),
	    cms.PSet(
	    	pluginType  = cms.string(pluginType),
	    	src		    = cms.InputTag(src),
	    	tag			= cms.string(legName+"PUIso"),
	    	method		= cms.string(legMethod+"particleIso()"),
	    	leadingOnly	= cms.untracked.bool(True)
	    ),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"LooseIsoDB"),
			method     = cms.string(legMethod+"tauID('byLooseIsolationDeltaBetaCorr')"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"MediumIsoDB"),
			method     = cms.string(legMethod+"tauID('byMediumIsolationDeltaBetaCorr')"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"LooseIsoCombDB"),
			method     = cms.string(legMethod+"tauID('byLooseCombinedIsolationDeltaBetaCorr')"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"MediumIsoCombDB"),
			method     = cms.string(legMethod+"tauID('byMediumCombinedIsolationDeltaBetaCorr')"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"TightIsoCombDB"),
			method     = cms.string(legMethod+"tauID('byTightCombinedIsolationDeltaBetaCorr')"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"EleVeto"),
			method     = cms.string(legMethod+"tauID('againstElectronLoose')"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"MuVeto"),
			method     = cms.string(legMethod+"tauID('againstMuonLoose')"),
			leadingOnly=cms.untracked.bool(True)
		),
		)
	return sharedV

def eleCommon(src,legName,legMethod,pluginType):
	sharedV = cms.VPSet(
		cms.PSet(
		   pluginType = cms.string(pluginType),
		   src        = cms.InputTag(src),
		   tag        = cms.string(legName+"Pt"),
		   method     = cms.string(legMethod+"pt"),
		   leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
		   pluginType = cms.string(pluginType),
		   src        = cms.InputTag(src),
		   tag        = cms.string(legName+"Eta"),
		   method     = cms.string(legMethod+"eta"),
		   leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
		   pluginType = cms.string(pluginType),
		   src        = cms.InputTag(src),
		   tag        = cms.string(legName+"Phi"),
		   method     = cms.string(legMethod+"phi"),
		   leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"elIso03B"),
			method     = cms.string("("+legMethod+"dr03TkSumPt()+max("+legMethod+"dr03EcalRecHitSumEt()-1.0,0.0)+"+legMethod+"dr03HcalTowerSumEt())/"+legMethod+"pt()"),
		    leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"RelIso03E"),
			method     = cms.string("("+legMethod+"dr03TkSumPt()+"+legMethod+"dr03EcalRecHitSumEt()+"+legMethod+"dr03HcalTowerSumEt())/"+legMethod+"pt()"),
		    leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"DcotTheta"),
			method     = cms.string(legMethod+'convDcot'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"ConvDistance"),
			method     = cms.string(legMethod+'convDist'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"MissHits"),
			method     = cms.string(legMethod+'gsfTrack().trackerExpectedHitsInner().numberOfHits()'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"RelPFIso"),
			method     = cms.string('('+legMethod+"chargedHadronIso+"+legMethod+"photonIso+"+legMethod+"neutralHadronIso)/"+legMethod+'pt()'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"IP"),
			method     = cms.string(legMethod+'dB'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"WP80"),
			method     = cms.string(legMethod+'userFloat("wp80")'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"WP90"),
			method     = cms.string(legMethod+'userFloat("wp90")'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"CiCLoose"),
			method     = cms.string(legMethod+'electronID("cicLoose")'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"CiCMedium"),
			method     = cms.string(legMethod+'electronID("cicMedium")'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"CiCTight"),
			method     = cms.string(legMethod+'electronID("cicTight")'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"CiCSuperTight"),
			method     = cms.string(legMethod+'electronID("cicSuperTight")'),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"CiCHyperTight1"),
			method     = cms.string(legMethod+'electronID("cicHyperTight1")'),
			leadingOnly=cms.untracked.bool(True)
		),
	  	cms.PSet(
		  	pluginType = cms.string(pluginType),
		  	src        = cms.InputTag(src),
		  	tag        = cms.string(legName+"RelPfIsoRho"),
		  	method     = cms.string("("+legMethod+"chargedHadronIso()+max("+legMethod+"photonIso()+"+legMethod+"neutralHadronIso()-"+legMethod+"userFloat('rho')*3.14*0.4*0.4,0.0))/"+legMethod+"pt()"),
		  	leadingOnly=cms.untracked.bool(True)
	  	),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"AbslPFIsoDB"),
			method     = cms.string("("+legMethod+"chargedHadronIso+max("+legMethod+"photonIso()+"+legMethod+"neutralHadronIso()-0.5*"+legMethod+"userIso(0),0.0))"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"RelPFIsoDB"),
			method     = cms.string("("+legMethod+"chargedHadronIso+max("+legMethod+"photonIso()+"+legMethod+"neutralHadronIso()-0.5*"+legMethod+"userIso(0),0.0))/"+legMethod+"pt()"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"StdIsoEcaldR03"),
			method     = cms.string(legMethod+"dr03EcalRecHitSumEt()"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"StdIsoEcal"),
			method     = cms.string(legMethod+"userIso(1)"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"StdIsoHcaldR03"),
			method     = cms.string(legMethod+"dr03HcalTowerSumEt()"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"StdIsoHcal"),
			method     = cms.string(legMethod+"userIso(2)"),
			leadingOnly=cms.untracked.bool(True)
		),
		cms.PSet(
			pluginType = cms.string(pluginType),
			src        = cms.InputTag(src),
			tag        = cms.string(legName+"StdIsoTk"),
			method     = cms.string(legMethod+"userIso(3)"),
			leadingOnly=cms.untracked.bool(True)
		),
	  	cms.PSet(
		  	pluginType = cms.string(pluginType),
		  	src        = cms.InputTag(src),
		  	tag        = cms.string(legName+"dB"),
		  	method     = cms.string(legMethod+"userIso(0)"),
		  	leadingOnly=cms.untracked.bool(True)
	  	)
		)
	return sharedV

def addMuMuTauTauEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
			coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
		zzShared = zzCommon(src,'PATMuMuTauTauQuadFiller'),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATMuMuTauTauQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("MuMuTauTauVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		#Candidate size quantities
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
		),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		#mumu quantities
#		mumuShared = muMuCommon(src,'PATMuMuTauTauQuadFiller'),
		z1l1 = muCommon(src,'z1l1','leg1.leg1.','PATMuMuTauTauQuadFiller'),
		z1l2 = muCommon(src,'z1l2','leg1.leg2.','PATMuMuTauTauQuadFiller'),
		#tautau quantities
		z2l1 = tauCommon(src,'z2l1','leg2.leg1.','PATMuMuTauTauQuadFiller'),
		z2l2 = tauCommon(src,'z2l2','leg2.leg2.','PATMuMuTauTauQuadFiller'),
#		tautauShared = tauTauCommon(src,'PATMuMuTauTauQuadFiller'),

#	    l1l1GenPt = cms.PSet(
#		  pluginType = cms.string("PATMuMuTauTauQuadFiller"),
#		  src        = cms.InputTag(src),
#		  tag        = cms.string("l1l1GenPt"),
#		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
#		  leadingOnly=cms.untracked.bool(True)
#	    ),
#	    l1l2GenPt = cms.PSet(
#		  pluginType = cms.string("PATMuMuTauTauQuadFiller"),
#		  src        = cms.InputTag(src),
#		  tag        = cms.string("l1l2GenPt"),
#		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
#		  leadingOnly=cms.untracked.bool(True)
#	    ),
#	  	l1GenMass = cms.PSet(
#		  pluginType = cms.string("PATMuMuTauTauQuadFiller"),
#		  src        = cms.InputTag(src),
#		  tag        = cms.string("l1GenMass"),
#		  method     = cms.string('leg1.p4VisGen().M()'),
#		  leadingOnly=cms.untracked.bool(True)
#	  	),
#	    l2l1GenPt = cms.PSet(
#		  pluginType = cms.string("PATMuMuTauTauQuadFiller"),
#		  src        = cms.InputTag(src),
#		  tag        = cms.string("l2l1GenPt"),
#		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
#		  leadingOnly=cms.untracked.bool(True)
#	    ),
#	    l2l2GenPt = cms.PSet(
#		  pluginType = cms.string("PATMuMuTauTauQuadFiller"),
#		  src        = cms.InputTag(src),
#		  tag        = cms.string("l2l2GenPt"),
#		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
#		  leadingOnly=cms.untracked.bool(True)
#	    ),
#	  	l2GenMass = cms.PSet(
#		  pluginType = cms.string("PATMuMuTauTauQuadFiller"),
#		  src        = cms.InputTag(src),
#		  tag        = cms.string("l2GenMass"),
#		  method     = cms.string('leg2.p4VisGen().M()'),
#		  leadingOnly=cms.untracked.bool(True)
#	  	),
#	  	GenMass = cms.PSet(
#		  pluginType = cms.string("PATMuMuTauTauQuadFiller"),
#		  src        = cms.InputTag(src),
#		  tag        = cms.string("GenMass"),
#		  method     = cms.string('p4VisGen().M()'),
#		  leadingOnly=cms.untracked.bool(True)
#	  	),
	)
	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)

#mumumumu tree
def addMuMuMuMuEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATMuMuMuMuQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("MuMuMuMuVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		#ZZ quantities
		zzShared = zzCommon(src,'PATMuMuMuMuQuadFiller'),
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
			),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
			),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
			),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		#mumu1 quantities
		z1l1 = muCommon(src,'z1l1','leg1.leg1.','PATMuMuMuMuQuadFiller'),
		z1l2 = muCommon(src,'z1l2','leg1.leg2.','PATMuMuMuMuQuadFiller'),
		z2l1 = muCommon(src,'z2l1','leg2.leg1.','PATMuMuMuMuQuadFiller'),
		z2l2 = muCommon(src,'z2l2','leg2.leg2.','PATMuMuMuMuQuadFiller'),
# 	    l1l1GenPt = cms.PSet(
# 		  pluginType = cms.string("PATMuMuMuMuQuadFiller"),
# 		  src        = cms.InputTag(src),
# 		  tag        = cms.string("l1l1GenPt"),
# 		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
# 		  leadingOnly=cms.untracked.bool(True)
# 	    ),
# 	    l1l2GenPt = cms.PSet(
# 		  pluginType = cms.string("PATMuMuMuMuQuadFiller"),
# 		  src        = cms.InputTag(src),
# 		  tag        = cms.string("l1l2GenPt"),
# 		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
# 		  leadingOnly=cms.untracked.bool(True)
# 	    ),
# 	  	l1GenMass = cms.PSet(
# 		  pluginType = cms.string("PATMuMuMuMuQuadFiller"),
# 		  src        = cms.InputTag(src),
# 		  tag        = cms.string("l1GenMass"),
# 		  method     = cms.string('leg1.p4VisGen().M()'),
# 		  leadingOnly=cms.untracked.bool(True)
# 	  	),
# 	    l2l1GenPt = cms.PSet(
# 		  pluginType = cms.string("PATMuMuMuMuQuadFiller"),
# 		  src        = cms.InputTag(src),
# 		  tag        = cms.string("l2l1GenPt"),
# 		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
# 		  leadingOnly=cms.untracked.bool(True)
# 	    ),
# 	    l2l2GenPt = cms.PSet(
# 		  pluginType = cms.string("PATMuMuMuMuQuadFiller"),
# 		  src        = cms.InputTag(src),
# 		  tag        = cms.string("l2l2GenPt"),
# 		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
# 		  leadingOnly=cms.untracked.bool(True)
# 	    ),
# 	  	l2GenMass = cms.PSet(
# 		  pluginType = cms.string("PATMuMuMuMuQuadFiller"),
# 		  src        = cms.InputTag(src),
# 		  tag        = cms.string("l2GenMass"),
# 		  method     = cms.string('leg2.p4VisGen().M()'),
# 		  leadingOnly=cms.untracked.bool(True)
# 	  	),
# 	  	GenMass = cms.PSet(
# 		  pluginType = cms.string("PATMuMuMuMuQuadFiller"),
# 		  src        = cms.InputTag(src),
# 		  tag        = cms.string("GenMass"),
# 		  method     = cms.string('p4VisGen().M()'),
# 		  leadingOnly=cms.untracked.bool(True)
# 	  	),
	)
	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)


#mumumutau tree
def addMuMuMuTauEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATMuMuMuTauQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("MuMuMuTauVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		#ZZ quantities
		zzShared = zzCommon(src,'PATMuMuMuTauQuadFiller'),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		z1l1 = muCommon(src,"z1l1","leg1.leg1.",'PATMuMuMuTauQuadFiller'),
		z1l2 = muCommon(src,"z1l2","leg1.leg2.",'PATMuMuMuTauQuadFiller'),
		z2l1 = muCommon(src,"z2l1","leg2.leg1.",'PATMuMuMuTauQuadFiller'),
		z2l2 = tauCommon(src,"z2l2","leg2.leg2.",'PATMuMuMuTauQuadFiller'),
	    l1l1GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l1GenPt"),
		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l1l2GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l2GenPt"),
		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l1GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1GenMass"),
		  method     = cms.string('leg1.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	    l2l1GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l1GenPt"),
		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l2l2GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l2GenPt"),
		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l2GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2GenMass"),
		  method     = cms.string('leg2.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	  	GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("GenMass"),
		  method     = cms.string('p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	)
	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)


#mumuelectau tree
def addMuMuEleTauEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATMuMuEleTauQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("MuMuEleTauVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		zzShared = zzCommon(src,'PATMuMuEleTauQuadFiller'),
		#ZZ quantities
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
		),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		#mumu quantities
#		mumuShared = muMuCommon(src,'PATMuMuEleTauQuadFiller'),
		z1l1 = muCommon(src,'z1l1','leg1.leg1.','PATMuMuEleTauQuadFiller'),
		z1l2 = muCommon(src,'z1l2','leg1.leg2.','PATMuMuEleTauQuadFiller'),
		z2l1 = eleCommon(src,'z2l1','leg2.leg1.','PATMuMuEleTauQuadFiller'),
		z2l2 = tauCommon(src,'z2l2','leg2.leg2.','PATMuMuEleTauQuadFiller'),
	    l1l1GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l1GenPt"),
		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l1l2GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l2GenPt"),
		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l1GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1GenMass"),
		  method     = cms.string('leg1.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	    l2l1GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l1GenPt"),
		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l2l2GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l2GenPt"),
		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l2GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2GenMass"),
		  method     = cms.string('leg2.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	  	GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("GenMass"),
		  method     = cms.string('p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	)

	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)
		
#mumuelemu tree
def addMuMuEleMuEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATMuMuEleMuQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("MuMuEleMuVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		#ZZ quantities
		zzShared = zzCommon(src,'PATMuMuEleMuQuadFiller'),
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
		),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		#mumu quantities
#		mumuShared = muMuCommon(src,'PATMuMuEleMuQuadFiller'),
		z1l1 = muCommon(src,'z1l1','leg1.leg1.','PATMuMuEleMuQuadFiller'),
		z1l2 = muCommon(src,'z1l2','leg1.leg2.','PATMuMuEleMuQuadFiller'),
		z2l1 = eleCommon(src,'z2l1','leg2.leg1.','PATMuMuEleMuQuadFiller'),
		z2l2 = muCommon(src,'z2l2','leg2.leg2.','PATMuMuEleMuQuadFiller'),
	    l1l1GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l1GenPt"),
		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l1l2GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l2GenPt"),
		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l1GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1GenMass"),
		  method     = cms.string('leg1.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	    l2l1GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l1GenPt"),
		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l2l2GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l2GenPt"),
		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l2GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2GenMass"),
		  method     = cms.string('leg2.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	  	GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("GenMass"),
		  method     = cms.string('p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
   )
   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)	

#mumueleele
def addMuMuEleEleEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATMuMuEleEleQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("MuMuEleEleVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		#ZZ quantities
		zzShared = zzCommon(src,'PATMuMuEleEleQuadFiller'),
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
		),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		#mumu quantities
#		mumuShared = muMuCommon(src,'PATMuMuEleEleQuadFiller'),
		z1l1 = muCommon(src,'z1l1','leg1.leg1.','PATMuMuEleEleQuadFiller'),
		z1l2 = muCommon(src,'z1l2','leg1.leg2.','PATMuMuEleEleQuadFiller'),
		z2l1 = eleCommon(src,'z2l1','leg2.leg1.','PATMuMuEleEleQuadFiller'),
		z2l2 = eleCommon(src,'z2l2','leg2.leg2.','PATMuMuEleEleQuadFiller'),
		
		#ele ele quantities
	    l1l1GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l1GenPt"),
		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l1l2GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l2GenPt"),
		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l1GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1GenMass"),
		  method     = cms.string('leg1.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	    l2l1GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l1GenPt"),
		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l2l2GenPt = cms.PSet(
		  pluginType = cms.string("PATMuMuEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l2GenPt"),
		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l2GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2GenMass"),
		  method     = cms.string('leg2.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	  	GenMass = cms.PSet(
		  pluginType = cms.string("PATMuMuEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("GenMass"),
		  method     = cms.string('p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	)
	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)


#eleeletautau
def addEleEleTauTauEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATEleEleTauTauQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("EleEleTauTauVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		#ZZ quantities
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
		),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		#ele ele quantities
		zzShared = zzCommon(src,'PATEleEleTauTauQuadFiller'),
		z1l1 = eleCommon(src,'z1l1','leg1.leg1.','PATEleEleTauTauQuadFiller'),
		z1l2 = eleCommon(src,'z1l2','leg1.leg2.','PATEleEleTauTauQuadFiller'),
		z2l1 = tauCommon(src,'z2l1','leg2.leg1.','PATEleEleTauTauQuadFiller'),
		z2l2 = tauCommon(src,'z2l2','leg2.leg2.','PATEleEleTauTauQuadFiller'),
	    l1l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleTauTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l1GenPt"),
		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l1l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleTauTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l2GenPt"),
		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l1GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleTauTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1GenMass"),
		  method     = cms.string('leg1.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	    l2l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleTauTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l1GenPt"),
		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l2l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleTauTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l2GenPt"),
		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l2GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleTauTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2GenMass"),
		  method     = cms.string('leg2.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	  	GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleTauTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("GenMass"),
		  method     = cms.string('p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	)
	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)

#eleeleeletau
def addEleEleEleTauEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATEleEleEleTauQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("EleEleEleTauVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		#ZZ quantities
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
		),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		zzShared = zzCommon(src,'PATEleEleEleTauQuadFiller'),
		z1l1 = eleCommon(src,'z1l1','leg1.leg1.','PATEleEleEleTauQuadFiller'),
		z1l2 = eleCommon(src,'z1l2','leg1.leg2.','PATEleEleEleTauQuadFiller'),
		z2l1 = eleCommon(src,'z2l1','leg2.leg1.','PATEleEleEleTauQuadFiller'),
		z2l2 = tauCommon(src,'z2l2','leg2.leg2.','PATEleEleEleTauQuadFiller'),

	    l1l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l1GenPt"),
		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l1l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l2GenPt"),
		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l1GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1GenMass"),
		  method     = cms.string('leg1.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	    l2l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l1GenPt"),
		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l2l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l2GenPt"),
		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l2GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2GenMass"),
		  method     = cms.string('leg2.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	  	GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleEleTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("GenMass"),
		  method     = cms.string('p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	)
	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)
	
#eleelemutau
def addEleEleMuTauEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATEleEleMuTauQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("EleEleMuTauVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		#ZZ quantities
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
		),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		zzShared = zzCommon(src,'PATEleEleMuTauQuadFiller'),
		z1l1 = eleCommon(src,'z1l1','leg1.leg1.','PATEleEleMuTauQuadFiller'),
		z1l2 = eleCommon(src,'z1l2','leg1.leg2.','PATEleEleMuTauQuadFiller'),
		z2l1 = muCommon(src,'z2l1','leg2.leg1.','PATEleEleMuTauQuadFiller'),
		z2l2 = tauCommon(src,'z2l2','leg2.leg2.','PATEleEleMuTauQuadFiller'),

	    l1l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l1GenPt"),
		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l1l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l2GenPt"),
		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l1GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1GenMass"),
		  method     = cms.string('leg1.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	    l2l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l1GenPt"),
		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l2l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l2GenPt"),
		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l2GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2GenMass"),
		  method     = cms.string('leg2.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	  	GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleMuTauQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("GenMass"),
		  method     = cms.string('p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	)
	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)
	
	
#eleeleelemu
def addEleEleEleMuEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATEleEleEleMuQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("EleEleEleMuVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		#ZZ quantities
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
		),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		zzShared = zzCommon(src,'PATEleEleEleMuQuadFiller'),
		z1l1 = eleCommon(src,'z1l1','leg1.leg1.','PATEleEleEleMuQuadFiller'),
		z1l2 = eleCommon(src,'z1l2','leg1.leg2.','PATEleEleEleMuQuadFiller'),
		z2l1 = eleCommon(src,'z2l1','leg2.leg1.','PATEleEleEleMuQuadFiller'),
		z2l2 = muCommon(src,'z2l2','leg2.leg2.','PATEleEleEleMuQuadFiller'),

	    l1l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l1GenPt"),
		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l1l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l2GenPt"),
		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l1GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1GenMass"),
		  method     = cms.string('leg1.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	    l2l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l1GenPt"),
		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l2l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l2GenPt"),
		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l2GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2GenMass"),
		  method     = cms.string('leg2.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	  	GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleEleMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("GenMass"),
		  method     = cms.string('p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	)
	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)
	

#eleeleeleele
def addEleEleEleEleEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATEleEleEleEleQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("EleEleEleEleVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		#ZZ quantities
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
		),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		zzShared = zzCommon(src,'PATEleEleEleEleQuadFiller'),
		z1l1 = eleCommon(src,'z1l1','leg1.leg1.','PATEleEleEleEleQuadFiller'),
		z1l2 = eleCommon(src,'z1l2','leg1.leg2.','PATEleEleEleEleQuadFiller'),
		z2l1 = eleCommon(src,'z2l1','leg2.leg1.','PATEleEleEleEleQuadFiller'),
		z2l2 = eleCommon(src,'z2l2','leg2.leg2.','PATEleEleEleEleQuadFiller'),

	    l1l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l1GenPt"),
		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l1l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l2GenPt"),
		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l1GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1GenMass"),
		  method     = cms.string('leg1.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	    l2l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l1GenPt"),
		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l2l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l2GenPt"),
		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l2GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2GenMass"),
		  method     = cms.string('leg2.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	  	GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleEleEleQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("GenMass"),
		  method     = cms.string('p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	)
	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)


def addEleEleMuMuEventTree(process,name,src = 'zzCleanedCandsAboveThreshold', srcEEEE='zzCleanedCandsAboveThreshold', srcEEMM='zzCleanedCandsAboveThreshold', srcMMEE='zzCleanedCandsAboveThreshold', srcMMMM='zzCleanedCandsAboveThreshold'):
	process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
	eventTree = cms.EDAnalyzer('EventTreeMaker',
		#common quantities
		coreCollections = cms.VInputTag(
			cms.InputTag(src)
		),
     	trigger = cms.PSet(
			pluginType = cms.string("TriggerFiller"),
			src        = cms.InputTag("patTrigger"),
			paths      = cms.vstring(TriggerPaths)
		),
		JetsPt20 = cms.PSet(
			pluginType = cms.string("PATEleEleMuMuQuadJetCountFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("jetsPt20"),
			method     = cms.string('pt()>20'),
			leadingOnly=cms.untracked.bool(True)
		),
		refitVertex = cms.PSet(
			pluginType = cms.string("EleEleMuMuVertexFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("refitVertex"),
			vertexTag  = cms.InputTag("offlinePrimaryVertices")
		),
		PVs = cms.PSet(
			pluginType = cms.string("VertexSizeFiller"),
			src        = cms.InputTag("primaryVertexFilter"),
			tag        = cms.string("vertices")
		),
		Rho = cms.PSet(
            pluginType = cms.string("EventWeightFiller"),
            src        = cms.InputTag("kt6PFJets","rho"),
            tag        = cms.string("rho")
        ),
		#ZZ quantities
		Size = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(src),
			tag        = cms.string("nZZCandidates"),
		),
		SizeEEEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEEE),
			tag        = cms.string("nZZeeeeCandidates"),
		),
		SizeEEMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcEEMM),
			tag        = cms.string("nZZeemmCandidates"),
		),
		SizeMMEE = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMEE),
			tag        = cms.string("nZZmmeeCandidates"),
		),
		SizeMMMM = cms.PSet(
			pluginType = cms.string("CollectionSizeFiller"),
			src        = cms.InputTag(srcMMMM),
			tag        = cms.string("nZZmmmmCandidates"),
		),
		zzShared = zzCommon(src,'PATEleEleMuMuQuadFiller'),
		z1l1 = eleCommon(src,'z1l1','leg1.leg1.','PATEleEleMuMuQuadFiller'),
		z1l2 = eleCommon(src,'z1l2','leg1.leg2.','PATEleEleMuMuQuadFiller'),
		z2l1 = muCommon(src,'z2l1','leg2.leg1.','PATEleEleMuMuQuadFiller'),
		z2l2 = muCommon(src,'z2l2','leg2.leg2.','PATEleEleMuMuQuadFiller'),

	    l1l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleMuMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l1GenPt"),
		  method     = cms.string('leg1.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l1l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleMuMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1l2GenPt"),
		  method     = cms.string('leg1.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l1GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleMuMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l1GenMass"),
		  method     = cms.string('leg1.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	    l2l1GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleMuMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l1GenPt"),
		  method     = cms.string('leg2.p4VisLeg1gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	    l2l2GenPt = cms.PSet(
		  pluginType = cms.string("PATEleEleMuMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2l2GenPt"),
		  method     = cms.string('leg2.p4VisLeg2gen().pt()'),
		  leadingOnly=cms.untracked.bool(True)
	    ),
	  	l2GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleMuMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("l2GenMass"),
		  method     = cms.string('leg2.p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	  	GenMass = cms.PSet(
		  pluginType = cms.string("PATEleEleMuMuQuadFiller"),
		  src        = cms.InputTag(src),
		  tag        = cms.string("GenMass"),
		  method     = cms.string('p4VisGen().M()'),
		  leadingOnly=cms.untracked.bool(True)
	  	),
	)
	setattr(process, name, eventTree)
	p = cms.Path(getattr(process,name))
	setattr(process, name+'Path', p)



