# calculates stats and has column
# heading as first item
def get_stats(score_list, entity):
    total_score = sum(score_list)
    best_score = max(score_list)
    worst_score = min(score_list)
    average = total_score / len(score_list)

    return [entity, total_score, best_score, worst_score, average]


# *** Main Routine starts here ****

# background formatting for heading, odd and even rows
head_back = "#FFFFFF"
odd_rows = "#C9D6E8"
even_rows = "yellow"

# User and computer scores
user_score = [20, 14, 14, 13, 14, 11, 20, 10, 20, 10]
computer_scores = [12, 4, 6, 20, 20, 14, 10, 14, 16, 12]

user_stats = get_stats(user_score, "User")
comp_stats = get_stats(computer_scores, "Computer")
row_names = ["", "Total", "Best Scene", "Worst Score", "Average_Score"]
row_formats = [head_back, odd_rows, even_rows, odd_rows, even_rows]

# transform stats lists, headings and formatting
# intp structure that can be used to make labels
all_labels = []

count = 0
for item in range(0, len(user_stats)):
    all_labels.append([row_names[item], row_formats[count]])
    all_labels.append([user_stats[item], row_formats[count]])
    all_labels.append([comp_stats[item], row_formats[count]])
    count += 1

print(all_labels)

