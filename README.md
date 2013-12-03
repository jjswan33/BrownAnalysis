BrownAnalysis
=============

Move of UWAnalysis from UW CVS to Git


Recipe:

scram pro -n MyWorkingAreaName CMSSW CMSSW_5_3_3

cd MyWorkingAreaName/src

cmsenv

git clone https://github.com/jjswan33/BrownAnalysis.git BrownAnalysis

cvs co -r V08-03-19      PhysicsTools/Utilities                           
cvs co -r V04-01-03      RecoLuminosity/LumiDB  
cvs co -r V02-01-00      HiggsAnalysis/CombinedLimit 

cvs co -r bMinimalSVfit-08-03-11 AnalysisDataFormats/TauAnalysis                  
cvs co -r V00-02-03s TauAnalysis/CandidateTools

cvs co -r   V05-00-16    DataFormats/JetReco



scramv1 b -j4
