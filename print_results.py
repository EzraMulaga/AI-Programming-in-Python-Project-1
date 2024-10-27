def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                   name (starting with 'pct' for percentage or 'n' for count)
                   and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """
    # Print model architecture
    print("\n*** Results Summary for CNN Model Architecture:", model.upper(), "***")
    
    # Print statistics
    print("\nStatistics:")
    print(f"{'Number of images':<30}: {results_stats_dic.get('n_images', 0)}")
    print(f"{'Number of dog images':<30}: {results_stats_dic.get('n_dogs_img', 0)}")
    print(f"{'Number of non-dog images':<30}: {results_stats_dic.get('n_notdogs_img', 0)}")
    print(f"{'Percentage of correct matches':<30}: {results_stats_dic.get('pct_match', 0.0):.2f}%")
    print(f"{'Percentage of correctly classified dogs':<30}: {results_stats_dic.get('pct_correct_dogs', 0.0):.2f}%")
    print(f"{'Percentage of correctly classified dog breeds':<30}: {results_stats_dic.get('pct_correct_breed', 0.0):.2f}%")
    print(f"{'Percentage of correctly classified non-dogs':<30}: {results_stats_dic.get('pct_correct_notdogs', 0.0):.2f}%")
    
    # Print misclassified dogs if print_incorrect_dogs is True
    if print_incorrect_dogs:
        print("\nIncorrectly Classified Dogs (Dog/Not-Dog Misclassifications):")
        for key in results_dic:
            # Pet image is a dog but classified as NOT a dog, or vice versa
            if results_dic[key][3] == 1 and results_dic[key][4] == 0:
                print(f"Pet label: {results_dic[key][0]:<20} | Classifier label: {results_dic[key][1]}")
            elif results_dic[key][3] == 0 and results_dic[key][4] == 1:
                print(f"Pet label: {results_dic[key][0]:<20} | Classifier label: {results_dic[key][1]}")

    # Print misclassified dog breeds if print_incorrect_breed is True
    if print_incorrect_breed:
        print("\nIncorrectly Classified Dog Breeds (Dog but Incorrect Breed):")
        for key in results_dic:
            # Pet image is a dog and classified as a dog, but breeds do not match
            if results_dic[key][3] == 1 and results_dic[key][4] == 1 and results_dic[key][2] == 0:
                print(f"Pet label: {results_dic[key][0]:<20} | Classifier label: {results_dic[key][1]}")
