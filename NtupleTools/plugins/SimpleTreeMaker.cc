#include "FWCore/Framework/interface/MakerMacros.h"
#include "BrownAnalysis/NtupleTools/plugins/SimpleTreeMaker.h"
#include "BrownAnalysis/DataFormats/interface/CompositePtrCandidateTMEt.h"
#include "BrownAnalysis/DataFormats/interface/CompositePtrCandidateTMEtFwd.h"
#include "BrownAnalysis/DataFormats/interface/CompositePtrCandidateT1T2MEt.h"
#include "BrownAnalysis/DataFormats/interface/CompositePtrCandidateT1T2MEtFwd.h"


typedef SimpleTreeMaker<pat::Tau> PATTauTree;


DEFINE_FWK_MODULE(PATTauTree);

