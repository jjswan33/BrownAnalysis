{
  gROOT->ProcessLine(".L UWAnalysis/ROOT/interactive/SimplePlotter.C+");
  gROOT->ProcessLine(".L UWAnalysis/ROOT/interactive/tdrstyle.C");
  setTDRStyle();
  
  SimplePlotter *plotter = new SimplePlotter();


  //   plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/EWK.root","diboson/t#bar{t}","0.9399*0.9444*__WEIGHT__",0,kRed+2,kRed+4);
  //    plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ZJETS.root","Z+jets","0.9399*0.9444*__WEIGHT__*(genTaus==0)",0,kMagenta-5,kMagenta+3);
  //   plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/QCD.root","QCD","2*0.9399*0.9444*__WEIGHT__",0,kViolet-5,kViolet+3);
  //   plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/W.root","W+jets","0.9399*0.9444*__WEIGHT__",0,kOrange+7,kOrange+3);
  // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ZJETS.root","Z +Jets","0.9399*0.9444*__WEIGHT__*(genTaus>0)",0,kOrange-2,kBlack);


  //    plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/QCD.root","QCD","2*__WEIGHT__*__CORR__",0,kMagenta-10,1);
  //    plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/VV.root","Diboson","__WEIGHT__*__CORR__*",0,kRed+2,1);
    plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/TOP.root","t#bar{t}","__WEIGHT__*__CORR__",0,kBlue-8,1);
    plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/W.root","W+jets","__WEIGHT__*__CORR__",0,kRed+2,1);
    plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/QCD.root","QCD","__WEIGHT__*2",0,kGreen+2,1);
    plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ZJETS.root","Z+jets","__WEIGHT__*__CORR__*(genTaus==0)",0,kOrange-4,kBlack);
    plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ZTT.root","Z#rightarrow #tau #tau","__WEIGHT__*__CORR__",0,kOrange-4,kBlack);

   //90
  //      plotter->addFile("muTauEventTreeNominal/eventTree","sandbox/ztt-latest/ggH90.root","#Phi(90) #rightarrow #tau #tau","90.2*__WEIGHT__",-1,kGreen+2,kGreen+2);
      //     plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA90.root","","87.7/110000",-1,5,1001);
   //   plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/ggH130.root","","1.53/110000",-1,5);
   //   plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA130.root","","0.04/106400",-1,5);

   //100
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/ggH100.root","#Phi(100) #rightarrow #tau #tau","54.5/110000",-1,5,1001);
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA100.root","","64.1/110000",-1,5,1001);
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/ggH130.root","","1.77/110000",-1,5);
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA130.root","","0.09/106400",-1,5);


  //STANDARD MODEL

    //         plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/sm115.root","10xSM H(115) #rightarrow #tau #tau","13.8*__WEIGHT__*__CORR__*__HQT__",-1,kBlue,kBlue);
    //         plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/vbf115.root","","1.07*__WEIGHT__*__CORR__",-1,kBlue,kBlue);
    //         plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/vh115.root","","0.971*__WEIGHT__*__CORR__",-1,kBlue,kBlue);

   

 // //   // // //120-40
 //        plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH120.root","#Phi(120) #rightarrow #tau #tau","39.73*__WEIGHT__",-1,kGreen+2,kGreen+2,1001); 
 //       plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA120.root","","64.93*__WEIGHT__",-1,kGreen+2,kGreen+2,1001); 
 //       plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH130.root","","2.91*__WEIGHT__",-1,kGreen+2,kGreen+2);
 //       plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA130.root","","1.04*__WEIGHT__",-1,kGreen+2,kGreen+2);


 // //   // // //120-30
            //      plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH120.root","#Phi(120) #rightarrow #tau #tau","HLT_Any*0.921*21.48*__WEIGHT__",-1,kGreen,1,1001); 
            // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH130.root","","HLT_Any*0.921*2.66*__WEIGHT__",-1,kGreen,1);
   
            //  plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA120.root","","HLT_Any*0.921*35.57*__WEIGHT__",-1,kGreen,1,1001); 
            //  plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA130.root","","HLT_Any*0.921*0.93*__WEIGHT__",-1,kGreen,1);

 // //   // // //120-15
    //      plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH120.root","#Phi(120,15) #rightarrow #tau #tau","0.9399*0.9444*4.91*__WEIGHT__",-1,kBlue,1,1001); 
    //      plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH130.root","","0.9444*0.9399*1.87*__WEIGHT__",-1,kBlue,1);
    // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA120.root","","0.9444*0.9399*8.48*__WEIGHT__",-1,kBlue,1); 
    // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA130.root","","0.9444*0.9399*0.53*__WEIGHT__",-1,kBlue,1);



   // //130
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/ggH130.root","#Phi(130) #rightarrow #tau #tau","16.4/110000",-1,5,1001);
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA130.root","","27.8/110000",-1,5,1001);

   // //140
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH140.root","#Phi(130) #rightarrow #tau #tau","10.17/110000",-1,5,1001);
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA140.root","","19.8/110000",-1,5,1001);
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH130.root","","1.39/110000",-1,5);
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA130.root","","1.39/106400",-1,5);


   // //160
     // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/ggH160.root","#Phi(160) #rightarrow #tau #tau","5.13/110000",-1,5,1001);
     // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA160.root","","12.96/110000",-1,5,1001);
     // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/ggH130.root","","1.24/110000",-1,5);
     // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA130.root","","0.23/106400",-1,5);

   // //180
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/ggH180.root","#Phi(180) #rightarrow #tau #tau","2.73/110000",-1,5,1001);
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA180.root","","8.44/110000",-1,5,1001);
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/ggH130.root","","1.19/110000",-1,5);
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA130.root","","0.10/106400",-1,5);

   // //200
                 // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH200.root","#Phi(200) #rightarrow #tau #tau","0.944*1.53*__WEIGHT__",-1,kRed,kBlack);
     	         // 	        plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA200.root","","0.944*5.65*__WEIGHT__",-1,kRed,1);
       		 //            plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH130.root","","0.9444*1.12*__WEIGHT__",-1,kRed,1);
       		 //            plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA130.root","","0.9444*0.06*__WEIGHT__",-1,kRed,1);


   // //250
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH250.root","#Phi(250) #rightarrow #tau #tau","0.43*__WEIGHT__",-1,kGreen+2,kGreen+2);
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA250.root","","2.28*__WEIGHT__",-1,kGreen+2,kGreen+2);
     // plotter->addFile("muTauEventTree/eventTrree","sandbox/ztt-latest/ggH130.root","","0.98*__WEIGHT__",-1,kGreen+2,kGreen+2);
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA130.root","","0.03*__WEIGHT__",-1,kGreen+2,kGreen+2);

   // //300
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/ggH300.root","#Phi(300) #rightarrow #tau #tau","0.14/110000",-1,5,1001);
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA300.root","","1.01/110000",-1,5,1001);
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/ggH130.root","","0.90/110000",-1,5);
    // plotter->addFile("muTauEventTree/eventTreeNominal","sandbox/ztt-latest/bbA130.root","","0.02/106400",-1,5);

   // //350,60
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH350.root","#Phi(350) #rightarrow #tau #tau","0.23*__WEIGHT__",-1,kBlue,kBlue);
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA350.root","","2.08*__WEIGHT__",-1,kBlue,kBlue);
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH130.root","","0.82*___WEIGHT__",-1,kBlue,kBlue);
     // plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA130.root","","0.01*__WEIGHT__",-1,kBlue,kBlue);

	      //	                 plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/DATA.root","DATA","1",1,kBlack,0);

  plotter->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/DATA.root","Observed","1",1,kBlack,0);

  SimplePlotter *plotterH = new SimplePlotter();

 //Higgs MC studies
  plotterH->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ZJETS.root","Z #rightarrow #tau #tau","__WEIGHT__*(genTaus>0)",-1,kBlue,kBlue,3004); 
  plotterH->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/sm120.root","ggH(120) #rightarrow #tau#tau","__WEIGHT__*__HQT__",-1,kRed,kRed,0);
  plotterH->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/vbf120.root","qqH(120) #rightarrow #tau #tau","__WEIGHT__",-1,kBlack,kBlack,0);


  SimplePlotter *plotterM = new SimplePlotter();

 //Higgs MC studies
  plotterM->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ZJETS.root","Z #rightarrow #tau #tau","__WEIGHT__*(genTaus>0)",-1,kBlue,kBlue,3004); 
  plotterM->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/TOP.root","t#bar{t}","__WEIGHT__",-1,kViolet-3,kViolet-3,0);
  plotterM->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/ggH120.root","ggA(120) #rightarrow #tau#tau","__WEIGHT__",-1,kRed,kRed,0);
  plotterM->addFile("muTauEventTree/eventTree","sandbox/ztt-latest/bbA120.root","bbA(120) #rightarrow #tau #tau","__WEIGHT__",-1,kBlack,kBlack,0);

















}
