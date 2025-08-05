# personal grade tracker
"""
Diffculty : beginner
time : 1 hour
concept : Basic dictionary operations,user input, data validation

## Requirements
1. store grades for multiple subjects
2. calculate average grade
3. find highest and lowest grades
4. display grade summary
5. add/update grades for subjects
"""
def add_grade(grades):
    """Add or update a grade for a subject.""" # Display header
    print("\n--- Add or Update Grade ---") # Display header
    subject = input("Enter the subject name: ").strip().title() # Get user input for subject
    try: # Get user input for subject
        grade = float(input(f"Enter the grade for {subject} (0-100): ")) # Get user input for grade
        if 0 <= grade <= 100: # Validate grade input
            if subject in grades: # Check if the subject already exists
                old_grade = grades[subject] # Store the old grade for updating
                grades[subject] = grade # Update the grade for the subject
                print(f"updated {subject}:{old_grade:.1f} to {grade:.1f}") # handle existing subject
            else:
                grades[subject] = grade # Add new subject with grade
                print(f"Added {subject}: {grade:.1f}") # handle new subject
        else:
            print("Grade must be between 0 and 100.") # handle invalid input
    except ValueError:
        print("Invalid input. Please enter a numeric grade.") # handle invalid input

def view_grades(grades):
    """Display all grades in a formatted table."""
    if not grades: # Check if grades dictionary is empty
        print("\nNo grades available.") # Display message if no grades are available
        return # Display header
    
    print(f"\n{'='*30}") # Display header
    print("Grade Summary") # Display header
    print(f"\n{'='*30}") # Display header
    print(f"{'Subject':<15} {'Grade':<8} {'Letter':<8}") # Display header
    print(f"{'-'*30}") # Display header

    for subject,grade in sorted(grades.items()): # Iterate through sorted grades
        Letter = get_letter_grade(grade) # Get letter grade
        print(f"{subject:<15} {grade:<8.1f} {Letter:<8}") # Display subject, grade, and letter grade
    
    print(f"{'-'*30}") # Display footer
    if grades:
        avg = sum(grades.values()) / len(grades) # Calculate average grade
        print(f"{'Average':<15} {avg:<8.1f} {'get_letter_grade(avg)':<8}") # Display average grade

def get_letter_grade(grade):
    """Convert numeric grade to letter grade."""
    if grade >= 97: # A+
        return "A+"
    elif grade >= 93: # A
        return "A"
    elif grade >= 90: # A-
        return "A-"
    elif grade >= 87: # B+
        return "B+"
    elif grade >= 83: # B
        return "B"
    elif grade >= 80: # B-
        return "B-"
    elif grade >= 77: # C+
        return "C+"
    elif grade >= 73: # C
        return "C"
    elif grade >= 70: # C-
        return "C-"
    elif grade >= 67: # D+
        return "D+"
    elif grade >= 65: # D
        return "D"
    else : # F
        return "F"

def calculate_average(grades):
    """Calculate and display average grade with motivational message."""
    if not grades: # Check if grades dictionary is empty
        print("\nNo grades available to calculate average.") # Display message if no grades are available
        return # Display header
    
    average = sum(grades.values()) / len(grades) # Calculate average grade
    letter = get_letter_grade(average) # Get letter grade

    print (f"\nGRADE ANALYSIS") # Display header
    print(f"{'='*25}") # Display header
    print(f"Average Grade: {average:.2f} ({letter})") # Display average grade and letter grade
    print(f"Total Subjects: {len(grades)}") # Display total number of subjects
    print(f"Total points: {sum(grades.values()):.1f}") # Display total points

    # Motivational message based on average grade
    
    if average >= 90:
        print("Excellent work! Keep it up!")
    elif average >= 80:
        print("Great job! You're doing well!")
    elif average >= 70:
        print("Good effort! Keep pushing!")
    else:
        print("Don't be discouraged! Every step counts. Keep improving!")

def find_extremes(grades):
    """Find and display highest and lowest grades."""
    if not grades:
        print("\nNo grades records available.") # Display message if no grades are available
        return # Display header
    
    best_subject = max(grades, key=grades.get) # Find subject with highest grade
    worst_subject = min(grades, key=grades.get) # Find subject with lowest grade
    best_grade = grades[best_subject] # Get the corresponding grades
    worst_grade = grades[worst_subject] # Get the corresponding grades

    print(f"\n Performance analysis") # Display header
    print(f"{'='*30}") # Display header
    print(f"Best Subject: {best_subject}") # Display best subject
    print(f"Grade: {best_grade:.1f} ({get_letter_grade(best_grade)})") # Display best subject and letter grade

    if best_subject != worst_subject: # Check if best and worst subjects are different
        print(f"Subject to Improve: {worst_subject}") # Display worst subject
        print(f"Grade: {worst_grade:.1f} ({get_letter_grade(worst_grade)})") # Display worst subject and letter grade
        improvment = best_grade - worst_grade # Calculate improvement needed
        print(f"Gap to close: {improvment:.1f} points") # Display gap to close
    else:
        print("you only have one subject, no comparison available.") # Display message if only one subject is present


def delete_grade(grades):
    """Delete a grade for a subject."""
    if not grades: # Check if grades dictionary is empty
        print("\nNo grades available to delete.") # Display message if no grades are available
        return # Display header
    
    print("\nCurrent Grades:") # Display header
    for i, subject in enumerate(grades.keys(),1): # Display current grades
        print(f"{i}. {subject} ({grades[subject]:.1f})") # Display subject and grade
    subject = input("Enter the subject name to delete: ").strip().title() # Get user input for subject
    if subject in grades:
        grade = grades.pop(subject) # Remove the subject from the dictionary
        print(f"Deleted {subject} (Grade: {grade:.1f})") # Display message for successful deletion
    else:
        print(f"{subject} not found in grades.") # Display message if subject not found

def grade_distribution(grades):
    """show grade distribution by letter grade."""
    if not grades: # Check if grades dictionary is empty
        print("\nNo grades available for distribution.") # Display message if no grades are available
        return
    
    distribution = {}
    for grade in grades.values(): # Iterate through grades
        letter = get_letter_grade(grade) # Get letter grade
        distribution[letter] = distribution.get(letter, 0) + 1 # Count occurrences of each letter grade
    
    print (f"\nGrade Distribution") # Display header
    print(f"{'='*25}") # Display header
    for letter in ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]:
        if letter in distribution:
            count = distribution[letter] # Get count for each letter grade
            percentage = (count / len(grades)) * 100 # Calculate percentage
            bar = "||" * (count // 3) # Create bar for visual representation
            print(f"{letter:<3}: {bar} {count} ({percentage:.1f}%)") # Display letter grade, bar, count, and percentage

def create_grade_tracker():
    """Main function to create and manage the grade tracker."""
    grades = {}  # Initialize an empty dictionary to store grades

    print("\nWelcome to the Personal Grade Tracker!")  # Welcome message
    print("Track your academic performance easily across subjects.\n")  # Description of the tool

    while True:  # Main loop for the grade tracker
        print(f"\n{'='*40}")  # Display header
        print("Personal Grade Tracker Menu")  # Display menu header
        print(f"{'='*40}")
        print("1. Add or Update Grade")  # Option to add or update grades
        print("2. View Grades")  # Option to view all grades
        print("3. Calculate Average Grade")  # Option to calculate average grade
        print("4. Find Highest and Lowest Grades")  # Option to find highest and lowest grades
        print("5. Grade Distribution")  # Option to view grade distribution
        print("6. Delete a Grade")  # Option to delete a grade
        print("7. Exit")
        print(f"{'='*40}")

        choice = input("Choose an option (1-7): ").strip()  # Get user input for menu choice
        if choice == '1':
            add_grade(grades)  # Call function to add or update a grade for a subject
        elif choice == '2':
            view_grades(grades)  # Call function to view all grades
        elif choice == '3':
            calculate_average(grades)  # Call function to calculate average grade
        elif choice == '4':
            find_extremes(grades)  # Call function to find highest and lowest grades
        elif choice == '5':
            grade_distribution(grades)  # Call function to show grade distribution
        elif choice == '6':
            delete_grade(grades)  # Call function to delete a grade
        elif choice == '7':
            print("Keep up the great work with your studies!")  # Exit message
            print("Remember, every step counts towards your success!")  # Motivational message
            break
        else:
            print("Invalid choice. Please select a valid option (1-7).")

        input("\nPress Enter to continue...")  # Wait for user input before continuing

if __name__ == "__main__":
    create_grade_tracker()  # Start the grade tracker application
# This code provides a simple personal grade tracker that allows users to manage their academic performance across multiple subjects.
# It includes features for adding/updating grades, viewing grades, calculating averages, finding extremes, and displaying grade distribution.
# The user interface is text-based and designed for easy interaction.