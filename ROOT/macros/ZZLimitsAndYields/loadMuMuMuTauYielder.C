{
	gROOT->ProcessLine(".L UWAnalysis/ROOT/macros/ZZLimitsAndYields/eventYields.C+");
	gROOT->ProcessLine(".L UWAnalysis/ROOT/interactive/tdrstyle.C");
	setTDRStyle();

	EventYield *MMMTyields = new EventYield();

	MMMTyields->addFile("muMuMuTauEventTreeID/eventTree","sandbox/zz-latest/DYJets.root","Zjets","__WEIGHT__",0,0.05);  
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ZZ4L.root","ZZ","__WEIGHT__",0,0.282);
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/DATA.root","DATA","1",1,137);
	
	MMMTyields->addFile("muMuMuTauEventTreeIDTauUp/eventTree","sandbox/zz-latest/DYJets.root","Zjets_CMS_scale_tUp","__WEIGHT__",10,0.05);  
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/zz-latest/ZZ4L.root","ZZ_CMS_scale_tUp","__WEIGHT__",10,0.282);
	
	MMMTyields->addFile("muMuMuTauEventTreeIDTauDown/eventTree","sandbox/zz-latest/DYJets.root","Zjets_CMS_scale_tDown","__WEIGHT__",10,0.05);  
	MMMTyields->addFile("muMuMuTauEventTreeTauDown/eventTree","sandbox/zz-latest/ZZ4L.root","ZZ_CMS_scale_tDown","__WEIGHT__",10,0.282);

	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH180.root","ggH180","__WEIGHT__",-1,137,"1.0*110","1.0*170");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH190.root","ggH190","__WEIGHT__",-1,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH200.root","ggH200","__WEIGHT__",-1,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH210.root","ggH210","__WEIGHT__",-1,137,"1.0*124","1.0*202");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH220.root","ggH220","__WEIGHT__",-1,137,"1.0*128","1.0*214");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH230.root","ggH230","__WEIGHT__",-1,137,"1.0*132","1.0*226");	
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH250.root","ggH250","__WEIGHT__",-1,137,"1.0*140","1.0*250");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH275.root","ggH275","__WEIGHT__",-1,137,"1.0*140","1.0*275");	
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH300.root","ggH300","__WEIGHT__",-1,137,"1.0*140","1.0*300");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH325.root","ggH325","__WEIGHT__",-1,137,"1.0*150","1.0*330");	
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH350.root","ggH350","__WEIGHT__",-1,137,"1.0*160","1.0*360");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH375.root","ggH375","__WEIGHT__",-1,137,"1.0*150","1.0*390");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH400.root","ggH400","__WEIGHT__",-1,137,"1.0*160","1.0*420");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH425.root","ggH425","__WEIGHT__",-1,137,"1.0*160","1.0*460");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH450.root","ggH450","__WEIGHT__",-1,137,"1.0*160","1.0*500");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH475.root","ggH475","__WEIGHT__",-1,137,"1.0*160","1.0*520");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH500.root","ggH500","__WEIGHT__",-1,137,"1.0*160","1.0*540");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH525.root","ggH525","__WEIGHT__",-1,137,"1.0*170","1.0*570");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH550.root","ggH550","__WEIGHT__",-1,137,"1.0*180","1.0*600");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH575.root","ggH575","__WEIGHT__",-1,137,"1.0*190","1.0*630");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/ggH600.root","ggH600","__WEIGHT__",-1,137,"1.0*200","1.0*660");
	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH180.root","ggH180_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*110","1.0*170");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH190.root","ggH190_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH200.root","ggH200_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH210.root","ggH210_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*124","1.0*202");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH220.root","ggH220_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*128","1.0*214");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH230.root","ggH230_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*132","1.0*226");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH250.root","ggH250_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*140","1.0*250");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH275.root","ggH275_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*140","1.0*275");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH300.root","ggH300_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*140","1.0*300");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH325.root","ggH325_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*150","1.0*330");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH350.root","ggH350_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*360");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH375.root","ggH375_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*150","1.0*390");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH400.root","ggH400_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*420");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH425.root","ggH425_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*460");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH450.root","ggH450_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*500");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH475.root","ggH475_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*520");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH500.root","ggH500_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*540");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH525.root","ggH525_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*170","1.0*570");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH550.root","ggH550_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*180","1.0*600");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH575.root","ggH575_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*190","1.0*630");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH600.root","ggH600_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*200","1.0*660");
	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH180.root","ggH180_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*110","1.0*170");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH190.root","ggH190_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH200.root","ggH200_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH210.root","ggH210_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*124","1.0*202");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH220.root","ggH220_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*128","1.0*214");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH230.root","ggH230_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*132","1.0*226");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH250.root","ggH250_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*140","1.0*250");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH275.root","ggH275_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*140","1.0*275");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH300.root","ggH300_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*140","1.0*300");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH325.root","ggH325_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*150","1.0*330");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH350.root","ggH350_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*360");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH375.root","ggH375_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*150","1.0*390");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH400.root","ggH400_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*420");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH425.root","ggH425_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*460");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH450.root","ggH450_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*500");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH475.root","ggH475_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*520");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH500.root","ggH500_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*540");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH525.root","ggH525_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*170","1.0*570");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH550.root","ggH550_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*180","1.0*600");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH575.root","ggH575_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*190","1.0*630");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/ggH600.root","ggH600_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*200","1.0*660");
	
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf180.root","vbf180","__WEIGHT__",-1,137,"1.0*110","1.0*170");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf190.root","vbf190","__WEIGHT__",-1,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf200.root","vbf200","__WEIGHT__",-1,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf210.root","vbf210","__WEIGHT__",-1,137,"1.0*124","1.0*202");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf220.root","vbf220","__WEIGHT__",-1,137,"1.0*128","1.0*214");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf230.root","vbf230","__WEIGHT__",-1,137,"1.0*132","1.0*226");	
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf250.root","vbf250","__WEIGHT__",-1,137,"1.0*140","1.0*250");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf275.root","vbf275","__WEIGHT__",-1,137,"1.0*140","1.0*275");	
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf300.root","vbf300","__WEIGHT__",-1,137,"1.0*140","1.0*300");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf325.root","vbf325","__WEIGHT__",-1,137,"1.0*150","1.0*330");	
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf350.root","vbf350","__WEIGHT__",-1,137,"1.0*160","1.0*360");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf375.root","vbf375","__WEIGHT__",-1,137,"1.0*150","1.0*390");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf400.root","vbf400","__WEIGHT__",-1,137,"1.0*160","1.0*420");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf425.root","vbf425","__WEIGHT__",-1,137,"1.0*160","1.0*460");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf450.root","vbf450","__WEIGHT__",-1,137,"1.0*160","1.0*500");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf475.root","vbf475","__WEIGHT__",-1,137,"1.0*160","1.0*520");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf500.root","vbf500","__WEIGHT__",-1,137,"1.0*160","1.0*540");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf525.root","vbf525","__WEIGHT__",-1,137,"1.0*170","1.0*570");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf550.root","vbf550","__WEIGHT__",-1,137,"1.0*180","1.0*600");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf575.root","vbf575","__WEIGHT__",-1,137,"1.0*190","1.0*630");
	MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/higgs-latest/vbf600.root","vbf600","__WEIGHT__",-1,137,"1.0*200","1.0*660");
	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf180.root","vbf180_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*110","1.0*170");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf190.root","vbf190_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf200.root","vbf200_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf210.root","vbf210_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*124","1.0*202");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf220.root","vbf220_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*128","1.0*214");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf230.root","vbf230_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*132","1.0*226");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf250.root","vbf250_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*140","1.0*250");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf275.root","vbf275_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*140","1.0*275");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf300.root","vbf300_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*140","1.0*300");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf325.root","vbf325_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*150","1.0*330");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf350.root","vbf350_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*360");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf375.root","vbf375_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*150","1.0*390");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf400.root","vbf400_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*420");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf425.root","vbf425_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*460");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf450.root","vbf450_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*500");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf475.root","vbf475_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*520");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf500.root","vbf500_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*160","1.0*540");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf525.root","vbf525_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*170","1.0*570");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf550.root","vbf550_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*180","1.0*600");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf575.root","vbf575_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*190","1.0*630");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf600.root","vbf600_CMS_scale_tUp","__WEIGHT__",10,137,"1.0*200","1.0*660");
	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf180.root","vbf180_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*110","1.0*170");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf190.root","vbf190_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf200.root","vbf200_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*120","1.0*190");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf210.root","vbf210_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*124","1.0*202");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf220.root","vbf220_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*128","1.0*214");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf230.root","vbf230_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*132","1.0*226");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf250.root","vbf250_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*140","1.0*250");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf275.root","vbf275_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*140","1.0*275");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf300.root","vbf300_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*140","1.0*300");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf325.root","vbf325_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*150","1.0*330");	
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf350.root","vbf350_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*360");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf375.root","vbf375_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*150","1.0*390");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf400.root","vbf400_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*420");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf425.root","vbf425_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*460");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf450.root","vbf450_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*500");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf475.root","vbf475_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*520");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf500.root","vbf500_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*160","1.0*540");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf525.root","vbf525_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*170","1.0*570");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf550.root","vbf550_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*180","1.0*600");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf575.root","vbf575_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*190","1.0*630");
	MMMTyields->addFile("muMuMuTauEventTreeTauUp/eventTree","sandbox/higgs-latest/vbf600.root","vbf600_CMS_scale_tDown","__WEIGHT__",10,137,"1.0*200","1.0*660");
	
	// // MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH120_presFix.root","H120","__WEIGHT__",-1,137,"0.6*80","0.6*120");
	// // MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH130_presFix.root","H130","__WEIGHT__",-1,137,"0.6*90","0.6*130");
	// // MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH140_presFix.root","H140","__WEIGHT__",-1,137,"0.6*110","0.6*160");
	// // MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH150_presFix.root","H150","__WEIGHT__",-1,137,"0.6*110","0.6*150");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH160_presFix.root","H160","__WEIGHT__",-1,137,"1.0*100","1.0*160");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH170_presFix.root","H170","__WEIGHT__",-1,137,"1.0*100","1.0*160");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH180_presFix.root","H180","__WEIGHT__",-1,137,"1.0*110","1.0*170");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH190_presFix.root","H190","__WEIGHT__",-1,137,"1.0*120","1.0*190");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH200_presFix.root","H200","__WEIGHT__",-1,137,"1.0*120","1.0*190");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH250_presFix.root","H250","__WEIGHT__",-1,137,"1.0*140","1.0*250");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH300_presFix.root","H300","__WEIGHT__",-1,137,"1.0*140","1.0*300");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH350_presFix.root","H350","__WEIGHT__",-1,137,"1.0*160","1.0*360");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH400_presFix.root","H400","__WEIGHT__",-1,137,"1.0*160","1.0*420");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH450_presFix.root","H450","__WEIGHT__",-1,137,"1.0*160","1.0*500");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH500_presFix.root","H500","__WEIGHT__",-1,137,"1.0*160","1.0*540");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH550_presFix.root","H550","__WEIGHT__",-1,137,"1.0*180","1.0*600");
	// MMMTyields->addFile("muMuMuTauEventTree/eventTree","sandbox/zz-latest/ggH600_presFix.root","H600","__WEIGHT__",-1,137,"1.0*200","1.0*660");
}
