#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py

# PROGRAMMER: Ezra Mulaga
# DATE CREATED: 29/07/2024                                
# REVISED DATE: 
# PURPOSE: Adjust results dictionary to indicate if labels are of-a-dog.

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int) where 1 = match between pet image
                    and classifier labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int) where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int) where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and pet image files. One dog name per line, all in lowercase. 
    Returns:
           None - results_dic is mutable, so no return needed.
    """
    # Read dog names from the file and store them in a set for fast lookup
    with open(dogfile, 'r') as f:
        dognames = set(line.strip() for line in f)

    # Process each entry in results_dic
    for key in results_dic:
        # Retrieve the pet and classifier labels
        pet_label = results_dic[key][0].lower()
        classifier_labels = results_dic[key][1].lower()

        # Determine if pet_label is a dog and add result at index 3
        if pet_label in dognames:
            results_dic[key].append(1)
        else:
            results_dic[key].append(0)

        # Determine if classifier_labels contains any dog name and add result at index 4
        if any(name.strip() in dognames for name in classifier_labels.split(', ')):
            results_dic[key].append(1)
        else:
            results_dic[key].append(0)
