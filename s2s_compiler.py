import random
import json
import re



class method():

    def __init__(self) -> None:
        pass

    @classmethod
    def readSettings(self,type) -> str:
        # Reading file name from settings.json
        with open("settings.json","r") as fobj:
            settings = json.load(fobj)
            fobj.close() 

        if type == "fileName":
            fileName = settings["fileName"]
            if fileName == "":
                fileName = settings["filePath"]
        
        return fileName

    @classmethod
    def readSource(self) -> str:
        # Reading soruce file contents
        with open(method.readSettings("fileName"),"r") as fobj:
            content = fobj.read()
            return content

    @classmethod
    def saveComp(self) -> None:
        # Writing to compiled file
        
        with open("settings.json","r") as fobj:
            settings = json.load(fobj)

        if settings["changeSource"]: # Source is changed itself 
            with open(method.readSettings("fileName"),"w") as fobj:
                fobj.write(compiler.source_content)
                fobj.close()
        elif not (settings["changeSource"]): # A new comp_ file is created``
            filePath = method.readSettings("fileName")
            pos = filePath.rfind("/") + 1
            fileName = filePath[pos:] 
            new_file = "comp_" + fileName
            
            with open(new_file,"w") as fobj:
                fobj.write(compiler.source_content)
                fobj.close()

    @classmethod 
    def cleanup(self):
        import os
        filesCreated = ["barrelRoll.py"]
        
        for i in filesCreated:
            os.remove(i)



class compiler():

    source_content = None   
    comp_content = None # currently not in use; only using source_content

    def __init__(self) -> None:
        method.cleanup()
        compiler.source_content = method.readSource()

    def main(self):
  
        E = easterEggs()
        
        E.han_greedo()
        E.meaning_of_life()
        E.bakers_dozen()
        E.flip_a_coin()
        E.roll_a_die()
        E.roll_a_dnd_dice()
        E.error418()
        E.once_in_a_blue_moon()
        E.horns_of_unicorn()
        E.look_in_the_mirror()
        E.mirrors_suck()
        E.do_a_barrel_roll()

        method.saveComp()



class easterEggs():

    def __init__(self) -> None:
        pass

    def han_greedo(self) -> None:
        pattern = "han shot first"
        repl = "greedo shot first"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def meaning_of_life(self) -> None:
        pattern0 = "what is the meaning of life"
        pattern1 = "answer to life the universe and everything"
        repl = "42"
        compiler.source_content = re.sub(pattern0,repl,compiler.source_content,flags=re.IGNORECASE)
        compiler.source_content = re.sub(pattern1,repl,compiler.source_content,flags=re.IGNORECASE)

    def bakers_dozen(self) -> None:
        pattern0 = "baker's dozen"
        pattern1 = "bakers dozen"
        repl = "13"
        compiler.source_content = re.sub(pattern0,repl,compiler.source_content,flags=re.IGNORECASE)
        compiler.source_content = re.sub(pattern1,repl,compiler.source_content,flags=re.IGNORECASE)

    def flip_a_coin(self) -> None:
        pattern = "flip a coin"
        coinFlip = ["heads","tails"]
        repl = random.choice(coinFlip)
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)
        
    def roll_a_die(self) -> None:
        pattern = "roll a die"
        dieRoll = ["1","2","3","4","5","6"]
        repl = random.choice(dieRoll)
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def roll_a_dnd_dice(self) -> None:
        pattern = "roll a d20"
        dieRoll = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14",'15","16',"17","18","19","Nat 20"]
        repl = random.choice(dieRoll)
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def error418(self) -> None:
        pattern = "Error 418"
        repl = "418. I'm a teapot \n The requested entity body is short and stout \n Tip me over and pour me out."
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def once_in_a_blue_moon(self) -> None:
        pattern = "once in a blue moon"
        repl = "1.1669016 x 10e-8 hertz" 
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def horns_of_unicorn(self) -> None:
        pattern = "the number of horns on a unicorn"
        repl = "1"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def loneliest_number(self) -> None:
        pattern = "what is the loneliest number"
        repl = "1"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def anagram(self) -> None:
        pattern = "anagram"
        repl = "nag a ram"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def recursion(self) -> None:
        # randomly capitalize letters
        pattern = "recursion"
        capital = random.sample(range(0,len(pattern)),4)
        repl = ""
        for index, i in enumerate(pattern):
            if index in capital:
                repl += i.upper()
            else:
                repl += i
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def hacker_language(self) -> None:
        pass

    def loch_ness_monster(self) -> None:
        pattern = "where is the loch ness monster"
        repl = "you can find Nessie at 57.323667970003704, -4.424191149125835 \n Also he is not a monster!"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def funniest_joke(self) -> None:
        pattern = "Wenn ist das Nunstück git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput! to English"
        repl = "[FATAL ERROR]"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def look_in_the_mirror(self) -> None:
        # reverse the whole doc string
        matchStatus = re.findall("I want to look in the mirror",compiler.source_content,flags=re.IGNORECASE)
        if matchStatus != None:
            if matchStatus!= []:
                compiler.source_content = compiler.source_content[::-1]
                if method.readSettings("changeSource"):
                    method.saveComp() 
                else:
                    method.saveComp()
                quit()
        else:
            pass

    def mirrors_suck(self) -> None:
        str = "mirrors suck"
        matchStatus = re.findall(str,compiler.source_content)
        keywords = ["print("]
        keywordStatus = False

        for i in keywords:
            if i in compiler.source_content:
                keywordStatus = True
                break

        if matchStatus != None and matchStatus!=[] and not keywordStatus:
            compiler.source_content = compiler.source_content[::-1] 
            if method.readSettings("changeSource"):
                method.saveComp()
            else:
                method.saveComp()
            quit()

    def do_a_barrel_roll(self) -> None:
        # write a function to a separate file and then replace the source print statement with an import statement  
        funcDef = """
def barrelRoll():
    import time
    tag = "I suck at ascii art so here's the best I can do"
    anim = [" |", " /", " -", " \\ "] * 10
    print(tag)
    for i in anim:
        time.sleep(0.25)
        print("Look at me do a barrel roll :",i,end="\\r")
        """

        repl = """import barrelRoll \nbarrelRoll.barrelRoll()"""
        pattern = '"do a barrel roll"'
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

        with open("barrelRoll.py","w") as fobj:
            fobj.writelines(funcDef)

    def negative_zero(self) -> None:
        pass





class functional():

    def __init__(self) -> None:
        pass

    def not_remainder(self) -> None:
        pass






if __name__ == "__main__":
    C = compiler()
    C.main()