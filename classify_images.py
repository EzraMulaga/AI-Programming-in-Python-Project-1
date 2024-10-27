#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py

# PROGRAMMER: Ezra Mulaga
# DATE CREATED: 29/07/2024                                 
# REVISED DATE: 
# PURPOSE: Defines the classify_images function that uses the classifier function 
#          to create classifier labels and compares them to pet image labels.

# Imports classifier function for using CNN to classify images
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. The function 
    formats classifier labels to match pet labels and compares them.
    
    Parameters: 
      images_dir - Full path to the folder of images to classify (string)
      results_dic - Dictionary with 'key' as image filename and 'value' as a list:
                    index 0 = pet image label (string)
                    index 1 = classifier label (string)
                    index 2 = 1/0 (int) indicating match (1) or no match (0)
      model - CNN model architecture for classification: 'resnet', 'alexnet', or 'vgg' (string)
    
    Returns:
      None - results_dic is mutable, so no return needed.
    """
    for filename in results_dic:
        # Use classifier function to get classifier label
        classifier_labels = classifier(images_dir + filename, model)

        # Format classifier label to match pet labels: lowercase and stripped of whitespace
        formatted_label = classifier_labels.lower().strip()

        # Retrieve pet label for comparison
        pet_label = results_dic[filename][0].lower()

        # Append the classifier label to results_dic
        results_dic[filename].append(formatted_label)

        # Compare pet label to classifier label and append match indicator (1 for match, 0 for no match)
        if pet_label in formatted_label:
            results_dic[filename].append(1)
        else:
            results_dic[filename].append(0)
