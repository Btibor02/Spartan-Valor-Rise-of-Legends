import sys, time, os
import items


def printSlow(str):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.02)



class Start():
    def intro():
        printSlow("\nIn the golden era of Ancient Greece, when gods and mortals walked the earth together, you find yourself amidst the majestic city-states, where myths and legends come to life.\n"
                "The air is thick with the scent of olive groves and the distant echoes of pantheons. Yet, beneath the divine splendor and scholarly wisdom lies a realm teeming with untold mysteries.")
        printSlow("\nYou, a daring young adventurer, have been chosen by the fates to embark on a heroic quest that will unravel the secrets of Olympus itself.\n" 
                "The gods, in their eternal wisdom, have sensed an impending darkness creeping over the land. Ancient prophecies speak of a chosen one who would rise to challenge the shadows and restore balance to the mortal realm.")
        printSlow("\nAs you set forth on this odyssey, you will uncover forgotten relics, decipher cryptic scrolls, and forge alliances with legendary heroes.\n" 
                "The echoes of your adventures will resound through the ages, leaving an indelible mark on the annals of Greek mythology.")
        printSlow("\nYour decisions will shape the fate of not just your own destiny, but the destiny of all Greece.")
        printSlow("\nPrepare to step into the sandals of a hero, for the fate of an entire civilization rests upon your shoulders.\n" 
                "The gods are watching, mortal, and Olympus trembles in anticipation. Will you rise to the challenge and become the stuff of legends?")
        printSlow("\nThe epic adventure of a lifetime awaits in the land where gods and heroes collide. Your journey begins now.\n")
        return
    
    def thalassa():
        printSlow("\nIn the heart of the ancient town, where marble columns stretched skyward and the aroma of incense lingered in the air, our hero sought counsel from the revered Oracle, Thalassa.\n" 
                  "Clad in robes adorned with intricate symbols of the gods, her eyes sparkled with ancient wisdom as she beckoned our hero to approach.")
        printSlow('\nThalassa, the keeper of secrets, gazed at the adventurer with a knowing smile.\n'
                  '"Ah, young one," she spoke, her voice carrying the weight of centuries. "I have sensed your quest, woven into the threads of fate. You seek the crypt of the lost hero, a place where shadows dance and legends sleep."')
        printSlow('\nWith a graceful motion, she extended her hand, revealing an ancient map etched with cryptic symbols.\n'
                  '"To find the crypt you seek," Thalassa continued, her words flowing like a sacred hymn, "you must venture to the sacred grove of Artemis, deep within the mystical Parnassus Forest.\n'
                  'There, beneath the moonlit branches, you shall find a stone altar adorned with the emblem of the owl—a symbol of wisdom."')
        printSlow("\nHer eyes bore into the hero's, a silent plea for understanding.\n"
                  '"Offer a prayer to Artemis, the goddess of the hunt and protector of the wild. If your intentions are pure and your heart is steadfast, she will guide you further. Beyond the sacred grove lies a hidden path, obscured from mortal eyes. Follow it, and it shall lead you to the entrance of the crypt you seek."')
        printSlow("\nYou nodded, gratitude and determination flickering in their eyes.\n"
                   '"Thank you, wise Thalassa," you said, your voice filled with respect. "I will heed your guidance and embark on this sacred journey."')
        printSlow("\nWith a serene smile, Thalassa raised her hand, tracing a protective sigil in the air.\n"
                    '"May the gods watch over you, brave one. Remember, in the realm of shadows, courage is your light, and wisdom is your sword. Go now, and may your steps be guided by the spirits of the ancients."')
        printSlow("\nAnd so, armed with Thalassa's knowledge and the blessings of the gods, you set forth towards the Parnassus Forest, ready to face the challenges that lay ahead and unveil the mysteries of the lost crypt.\n")
        return
    
    def parnassusForest(chance, first):
        if first == True:
                printSlow("\nA dense, ancient woodland shrouded in a tapestry of towering trees and vibrant foliage. Sunlight filters through the canopy, creating a mosaic of light and shadow on the moss-covered ground. ")
                printSlow("The air is rich with the fragrance of blooming flowers and pine. The forest's atmosphere is both serene and mysterious, with occasional glimpses of wildlife and a sense that the trees themselves hold untold secrets. ")
                printSlow("You found a chest half-concealed by leaves. Carved with ancient symbols, it beckons with mystery.\n")
                print(items.Items.chestWithLeaf())
                if chance < 7:
                        printSlow("\nOpening it reveals treasures — a set of scrolls, some gold, and a map hinting at uncharted territories.\n")
                elif chance >= 7:
                        printSlow("\nOpening it reveals treasures — a set of scrolls, some gold, a map hinting at uncharted territories, and a spear.\n")
        elif first == False:
                printSlow("\nYou follow the enchanted map to the sacred grove of Artemis. A hidden path materializes, guiding them toward the entrance of the crypt. With the forest as their silent ally, the hero approaches the looming shadows, sword raised, ready to unveil the mysteries concealed within. \n")
                time.sleep(5)
                printSlow("A lone figure emerges from the shadows of the Parnassus Forest, a skilled guardian known as the Forest Sentinel. Cloaked in a mantle woven from the forest's secrets, this solitary archer moves with the grace of the ancient trees. ")
                printSlow("\nTo continue your journey, you must defeat the sentinel in a battle\n")
                time.sleep(5)

        return
        