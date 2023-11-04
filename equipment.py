class Weapons:
    def Kolós():
        name = "Kolós"
        image = """  
            &/        
            %@%        
        &%*&%*&%*       
            %&/        
        &%*&%*&%*        
            %%(        
            %#(        
            %%/        
            %#*        
            %%/        
            #%*        
            ##,        
            *%,     """
        damage = 3
        durability = 100
        description = "Clubs were simple, blunt weapons made of wood or metal. While not as common as other weapons, they were still used in battle, especially in earlier periods"

        return name, image, damage, durability, description

    def Dory():
        name = "Dory"
        image = """  
                                                        &&&@&  
                                                    &&&&@&&     
                                                .&&&@@&&         
                                        &    %&@@&&             
                                        (%@@                    
                                    .//#&   %                    
                                //#&.                            
                            .//#%                                 
                        *//#                                      
                    /*/#%                                          
                (/(%.                                              
            *//%&  """
        damage = 5.5
        durability = 250
        description = "The spear was the primary weapon of Greek soldiers, particularly the hoplites. It had a wooden shaft and a metal spearhead, typically made of bronze. The spear was used for thrusting and throwing."

        return name, image, damage, durability, description
    
    def Xiphos():
        name = "Xiphos"
        image = """  
                                                  *,( 
                                                  &%(   
                                              &%#&     
                                        **  &%&(       
                                        *****          
                                      ***,,,, /.        
                                    ***,,,              
                                ,**,..,                
                              **,...                   
                            **,,..*                     
                          **,,..                        
                      **,,...                          
                    .**,,..                             
                  ***,,..                               
                ***,,,                                  
              **,.,/                                    
            *,..,                                       
          *,.                                           
        */ """
        damage = 8
        durability = 275
        description = "The xiphos was a short, double-edged sword with a leaf-shaped blade. It was a secondary weapon for Greek soldiers, often used in close combat."

        return name, image, damage, durability, description
    
    def Labrys():
        name = "Labrys"
        image = """
                                ,.                 
                           //*,*.,                
                          /*/***,                 
                         ,/*,  *, *               
                          .     &&./#             
                              &%&   ,,.           
                           *&%&     ,,.   /       
                         &%&.     ..    (         
                       %%&                        
                    &%%&                          
                  %#&                             
                %#%                               
             %%%(                                 
           %#&                                    
        *%%&    """
        damage = 11
        durability = 150
        description = "The labrys was a double-headed axe and was mainly used as a ceremonial or symbolic weapon. It had religious significance in some cultures, such as the Minoans."

        return name, image, damage, durability, description
    
class Shields:
    def AspisOfHoplon():
        name = "Aspis of Hoplon"
        image = """
                /%(//(/((###%&&&%                
              %&#(*./**(((((/(/#%%%&&             
            #(#/*,, .,,*(##%##/,,,.(#&&           
          %#%#(*.*/%#(//(/*(#((((*,,,/(#%         
         %%((#/#(((%##&/#(/##%(/#(/**/((%%        
        (((((#(%(/(*/((/((/(,%%(##///,*/#%%       
        #(##(%%%##(%/*%%%(##%/*/*#(%//(((/%       
        %##%%%##(%#&#%%#(%#/#%#/#%#((##((#%       
         #((###%%%,%%###%&#&#%%/%(%#((#((&        
         (###((#%%&&@&##(%&&&(#(/((((((&%         
           %%#####%%&%%&%@%##(##(((((%%%          
             ####&&@@@&##%#%&%&&&#%%&@            
               (#%&&@@@@@@&&&%  %#&(     """
        shield = "1"
        durability = 100
        description = "The aspis or hoplon was a large, round shield made of wood and covered with bronze. It was an essential defensive tool used by hoplites, providing protection for the warrior and forming a phalanx formation with other soldiers."

        return name, image, shield, durability, description
    
    def Pelte():
        name = "Pelte"
        image = """
              */****,,..,.***///(//(              
         *,,,*(*,,,,,,,,,*****/////**////(,       
         (*..,,..      .....,**////*,,**.((       
         ,....,..      .....,,**////*,,*(/.       
         *.#.....          .****///**,,*//,       
         ..*....           ..,,*////*,,*/(        
          ,,.,,.          ..,,,*////*** /(        
          /.,,,..        .,,,**/////*,,//         
           ,,,,,.      ....,,*////(/** /(         
           *#/*,..   ..  .,***//////***(          
            *,(,,.......,,**////((//*/*#          
             /**,,....,,,,**///((/(//*.           
              **/,,,,,...,,***/(((((/.            
               /*,,,,,,****//((((((((             
                .*********/(((((.((               
                  /#//*//////(((#(                
                    //////(((#(.                  
                      (/((/((.                    
                        (.#(        """
        shield = "3"
        durability = "175"
        description = "The pelte was a crescent-shaped shield, often associated with light infantry and skirmishers such as peltasts. It was smaller and lighter than the hoplon, providing mobility for troops who needed to move quickly on the battlefield. The pelte was typically made of wood and covered with leather."

        return name, image, shield, durability, description
    
    def Thureos():
        name = "Thureos"
        image = """
                        ,*..,*                      
                    .*,,,*,,..,**//**.                
        ,*****(/*,*,,,/*,,,.*,**/*,,,,*/(((////,.    
        *#/////((/***,,//*,,,,***/*,,,,,*/(//((((#*   
        *%///*(#(/****,//*,,/***//*,,*,**/((,((((#*   
        *#///((((/****,*/*,*////(/*,,*,,*/((/(###(,   
        *#/(((#((/*(,,,**%***/*%**,,****//((//(##(,   
        *#((((#((//,//*((#///////*////,*/(((//###(,   
        *#((/,(((//,/,/(//*#(****#//**,*/(#(,(#%#/,    
        *%((((((((/,(,#(/,((/(/(/***,.**//////((%/    
        .&(((((((((/,//(#//*%#%*&/**.,,*//*////(%(    
        (##((((((((/,***////(((//,.,,,***,////((,    
        ,%((((((/(//**,,/*//((#*,,,,,,*,,***//#/     
          ,/(////////******/%/%#/***,.,,,,***/,*      
            *(/////(,*,,***/(/#(//**.....,,*/(.       
            .*(/*//**,,,**///#(/**,......,(.         
                /,(/**,,,,*/,((//*,....,/,            
                  ./,(/*,,*(/((**,,*./,               
                      ,*,(##//(,*/.                   
                          .,*.                        """
        shield = "5"
        durability = "200"
        description = "The thureos was a rectangular or oval-shaped shield that became popular during the Hellenistic period. It had a curved surface and was slightly concave, providing better protection than some other shield types."

        return name, image, shield, durability, description
    

class Potions:
    def Heal():
        name = "Heal potion"
        image = """
                *,%/(,#                
                ,//(#(%(#               
                #(*%%####               
                ..*/(%#..               
                 *. . .*                
                 *.   .*                
                 *.  ..*                
                 *.. ..,                
                ,........               
               .,*,,,,,*,,              
            ,..,.........,..,           
         ,,*,,##////////(#(,,,**.       
       .#**(#/,,,(((((###%##(//*#.      
      .,**//////((#######%#(/(//**.     
      ,/##/((#############%#((((#*.     
      .//((((###########%%%###((/*.     
       ,*/(((########%#%%#%##((/*,      
       ,//((((#(#(#######((#((/*       
         .*/((#((###########((/.        
            ,/############%%/           
              ..,,/@@&&@*,...        
              ...,,,,,,,.....    """
        ability = 20
        quantity = 3
        description = "+20 HP"

        return name, image, ability, quantity, description
    
    def Shield():
        name = "Shield potion"
        image = """
                             
                 #/////#                
                 .(/((#                 
                .    ....               
                .........               
                #/.....#,               
                ........(.              
          ................#/...         
        ..... ..... , .../,,,,,..       
        .##/ ///..////////,,,,,,.       
        .%%/ //////////////,,,,,*       
        .(%( (*(((((((((((%,,,,,/       
         ..%((((((((((/*((%/%&(.        
           .,%(((/*((((((#%%..          
             ..%(((((((%%%..            
                .........     """

        ability = 20
        quantity = 2
        description = "+20 Shield"

        return name, image, ability, quantity, description


class Others:
    def Key():
        name = "Key"
        image = """
                                  */                                
                                /#   &&%/.                           
                              #&&%%&&&&&%%%                         
                            #&#*&%#(% &&(#(                         
                            (%#&%%#&&  %% #&                         
                        ##%%#&%&&&#(%&%  ((                          
                  ##/#&&%%%,    &  &%%%%(                           
            (#%(&&%&                                                
        &%%&&%#                                                     
        %&&%                                                        
          &*                                                        
                """
        description = "What could it open?"

        return name, image, description
