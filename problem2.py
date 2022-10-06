def freq_dictionary(infile):
    """
        Takes a text file and creates a dictionary with key-value pairs
        with the number of appearances of a word.
    """

    file = open(infile, 'r')
    data = file.read()
    freq_dict = {}

    for word in data.split():
        word = word.lower()
        print(word)
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1

    # for line in data:
    #     words = line.split(" ")
    #     for word in words:
    #         word = word.strip().lower()
    #         print(word)
    #         
    
    print(freq_dict)

    file.close()
    
    return freq_dict



def cosine_similarity(docfile1, docfile2):
    """
        Takes two text files, creates a dictionary of word frequencies,
        and finds the cosine similarity of the two.
    """
    # Open both files for reading

    # file_1 = open(docfile1, 'r')
    # file_2 = open(docfile2, 'r')

    file_1_dict = freq_dictionary(docfile1)
    file_2_dict = freq_dictionary(docfile2)

    # Cosine Similarity





freq_dictionary("doc3.txt")
# cosine_similarity('doc2.txt','doc3.txt')