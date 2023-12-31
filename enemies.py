class Enemies():
    def mannequin():
        name = "Mannequin"
        image = """
                ,*(#(((//                         
               /*(#%%/##(/**            
                ///*//*//((             
                /((((((((/              
              ***/(((((///*             
          .******///////*****/.         
    *,,,******/////////////*******,,    
   ///////////////////////////*/******* 
     (//(////////////////////////(//(   
       (/////////////////////////((     
       (/////***////////////////((      
        ////////***////**//////((       
         //////////*****/**////(        
          //////***********///(                 
         ////*//*///////***/*///        
              @@@&&&@&&@@@@                        
              &&&&&&@&%@@@#             
              @&@&&&@@&@@@.             
              *@@@&@@@@@@@/.            
      ###%%%%&@@@@&@@@&@@@@&@&&#%       
  .%@@&&&&@&&&@@@@@@@@@@@@@@@@@@@&&&&&  
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*   
        @@@@@@@@@@@@@@@@@@@@@@@&.  """

        damage = 0
        block = 0
        hp = 30

        return name, image, damage, block, hp
    
    def forestSentinel():
        name = "Forest Sentinel"
        image = """                                                   
                           *   &                            
                      * (  (#,                              
                       *  ./ **(###  #  %                   
                    %  #(( (%##%   /*                       
                 #*  //  /%/.#/, ( /                        
                     /(  //((**.,((/                        
                        /( (#.. /  (*                       
                      ((    (*,*     (/                     
                   //&(     (#*#       %.                   
                  /*(      #%##(/        *                  
                */#        /#//,/         ,                 
               (/           ###(/         .*                
              (             #%((           *.               
              (.            (((/#        /  .               
              (.            #%@#%                           
                (           (#&%#                           
                /           (%&&%&                          
                            &%&%%&                          
                            &@@@@#                          
                         &%&@&%%@@&&                        
                         .  . . ,&&.#& """
        damage = 5
        block = 2
        hp = 20

        return name, image, damage, block, hp