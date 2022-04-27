import re

class Moby_Preprocessing():

  def stackoverflow_greenberg(text):
    '''
    This function is copied from:
    https://stackoverflow.com/a/31505798
    It splits the text file into a list of complete sentences.
    '''
    import re
    alphabets= "([A-Za-z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|Mt)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov|me|edu)"

    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

  def clean_hyphens(text):
    if not text:
      return text
    
    while text[0] == "-":
      text = text[1:]
    
    return text

  def __init__(self):
    moby_path =  tf.keras.utils.get_file('/tmp/moby.txt', 
                                          origin='https://www.gutenberg.org/files/2701/old/moby10b.txt')

    moby_text = open(moby_path).read()
    sentences = Moby_Preprocessing.stackoverflow_greenberg(moby_text)
    sentences = sentences[381:] # Starts from Chapter 1
    sentences = [sentence for sentence in sentences if "CHAPTER" not in sentence]
    sentences = [Moby_Preprocessing.clean_hyphens(sentence) for sentence in sentences]

    self.sentences = sentences
  
  if __name__ == "__main__":
    import doctest
    doctest.testmod()