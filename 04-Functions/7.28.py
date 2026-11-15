def f(dice):
    current_dice = ""
    current_count = 0
    best_dice = ""
    best_count = 0

    for d in dice:
        if d == current_dice:
            current_count += 1
        else:
            current_dice = d
            current_count = 1

        if current_count > best_count:
            best_count = current_count
            best_dice = current_dice

    return int(best_dice)