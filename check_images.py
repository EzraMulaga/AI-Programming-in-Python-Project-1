#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: Ezra Mulaga
# DATE CREATED: 17/07/2024
# REVISED DATE:
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          Note that the true identity of the pet (or object) in the image is
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this
#          program, we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time

# import check modules
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Measures total program runtime by collecting start time
    start_time = time()

    # Retrieve command line arguments
    in_arg = get_input_args()
    
    check_command_line_arguments(in_arg)

    # Get pet labels from the specified directory
    results = get_pet_labels(in_arg.dir)
    
    check_creating_pet_image_labels(results)

    # Classify images using the specified CNN model architecture
    classify_images(in_arg.dir, results, in_arg.arch)
    
    check_classifying_images(results) 

    # Adjust results to determine if correctly classified as 'a dog'
    adjust_results4_isadog(results, in_arg.dogfile)
    
    check_classifying_labels_as_dogs(results)

    # Calculate results statistics and summarize them
    results_stats = calculates_results_stats(results)
    
    check_calculating_results(results, results_stats)

    # Print results including statistics and incorrectly classified cases
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measures total program runtime by collecting end time
    end_time = time()

    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\nTotal Elapsed Runtime:", str(int((tot_time / 3600))) + ":" +
          str(int(((tot_time % 3600) / 60))) + ":" +
          str(int(((tot_time % 3600) % 60))))

# Call to main function to run the program
if __name__ == "__main__":
    main()
