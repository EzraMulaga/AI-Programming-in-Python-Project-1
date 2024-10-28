#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results_hints.py
#                                                                             
# PROGRAMMER: Ezra Mulaga
# DATE CREATED: 25/10/2024
# REVISED DATE: 28/10/2024
# PURPOSE: Prints results statistics and misclassified cases (dogs/breeds)
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and optionally prints incorrectly 
    classified dogs and incorrectly classified dog breeds if specified.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index) idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int) where 1 = match between labels, 0 = no match
                    idx 3 = 1/0 (int) where 1 = pet image 'is-a' dog, 0 = 'is-NOT-a' dog 
                    idx 4 = 1/0 (int) where 1 = Classifier 'as-a' dog, 0 = 'as-NOT-a' dog
      results_stats_dic - Dictionary of results statistics with key as statistic name 
                          (starting with 'pct' for percentage or 'n' for count) and 
                          value as the statistic's value
      model - CNN model architecture used by classifier (string; 'resnet', 'alexnet', 'vgg')
      print_incorrect_dogs - If True, prints incorrectly classified dogs (bool)  
      print_incorrect_breed - If True, prints incorrectly classified dog breeds (bool) 

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
    
    # Counters for correct classifications
    correct_dogs = 0
    correct_not_dogs = 0
    correct_dog_breeds = 0

    # Print misclassified dogs if print_incorrect_dogs is True
    if print_incorrect_dogs:
        print("\nIncorrectly Classified Dogs (Dog/Not-Dog Misclassifications):")
        for key in results_dic:
            # Pet image is a dog but classified as NOT a dog
            if results_dic[key][3] == 1 and results_dic[key][4] == 0:
                print(f"Pet label: {results_dic[key][0]:<20} | Classifier label: {results_dic[key][1]}")
            # Pet image is NOT a dog but classified as a dog
            elif results_dic[key][3] == 0 and results_dic[key][4] == 1:
                print(f"Pet label: {results_dic[key][0]:<20} | Classifier label: {results_dic[key][1]}")
            
            # Counting correct classifications
            if results_dic[key][3] == 1 and results_dic[key][4] == 1:
                correct_dogs += 1  # Correctly classified as a dog
                # Check if the breed also matches
                if results_dic[key][2] == 1:
                    correct_dog_breeds += 1
            elif results_dic[key][3] == 0 and results_dic[key][4] == 0:
                correct_not_dogs += 1  # Correctly classified as not a dog

        # Total number of images
        total_images = len(results_dic)

        # Check if correct classifications match the total images
        if (correct_dogs + correct_not_dogs) != total_images:
            print("\nWarning: The number of correctly classified dogs and not-dogs does not match the total number of images.")
            print(f"Correctly classified dogs: {correct_dogs}")
            print(f"Correctly classified not-dogs: {correct_not_dogs}")
            print(f"Total images: {total_images}")

    # Check and print misclassified breeds if print_incorrect_breed is True
    if print_incorrect_breed and correct_dogs != correct_dog_breeds:
        print("\nIncorrectly Classified Dog Breeds (Dog but Incorrect Breed):")
        for key in results_dic:
            # Pet image is a dog and classified as a dog, but breeds do not match
            if results_dic[key][3] == 1 and results_dic[key][4] == 1 and results_dic[key][2] == 0:
                print(f"Pet label: {results_dic[key][0]:<20} | Classifier label: {results_dic[key][1]}")

        # Print a summary of correct and incorrect breed classifications
        print(f"\nSummary of Dog Breed Classifications:")
        print(f"Correctly Classified Dogs: {correct_dogs}")
        print(f"Correct Dog Breeds: {correct_dog_breeds}")
        print(f"Incorrect Dog Breeds: {correct_dogs - correct_dog_breeds}")
