#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py

# PROGRAMMER: Ezra Mulaga
# DATE CREATED: 18/07/2024                                 
# REVISED DATE: 
# PURPOSE: Define get_pet_labels function to create pet labels from image filenames.

from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
    
    in_files = listdir(image_dir)
    results_dic = dict()

    for filename in in_files:
        if filename[0] != ".":  # ignore hidden files
            pet_label = ""
            word_list = filename.lower().split('_')
            pet_label = ' '.join([word for word in word_list if word.isalpha()]).strip()

            # Store pet label in results_dic with filename as key
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print("** Warning: Duplicate file found in directory:", filename)

    return results_dic
