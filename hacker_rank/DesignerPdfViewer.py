def designerPdfViewer(h, word):
    h=h.split(' ')
    w_sizes = map(lambda x: h[(ord(x)+0-ord('a'))], word) 
    print(len(word)* max(list(map(int,list(w_sizes)))))


designerPdfViewer(
    "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7", "zaba")
