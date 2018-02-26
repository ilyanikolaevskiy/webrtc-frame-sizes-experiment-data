
# Processes an analyzes debug output of the webrtc screenshare_loopback tool.
# Input file format:
# each line has 3 space-sparated numbers: frame_size, target_size, and ratio.
# if all the numbers are -1, this line indicates the slide change event.
# otherwise it contains frame size, target frame size to their ratio for the
# encoded frame. 
# Output:
# Maximum frame size ratio for non slide change and minimum frame size ratio for 
# the slide change.
# For each ratio from 2 to 4 with step 0.0.5 shows how much in percent false positive
# and false negatives are present.

file = open("data.txt", "rt");
new_slide = True
slide_changes_ratios = []
normal_ratios = []
for line in file:
  frame_size, target_size, ratio = line.split()
  frame_size = int(frame_size)
  target_size = int(target_size)
  ratio = float(ratio)
  if frame_size == -1:
    new_slide = True
  else:
    if (new_slide):
      slide_changes_ratios.append(ratio)
    else:
      normal_ratios.append(ratio)
    new_slide = False

print min(slide_changes_ratios), max(normal_ratios)

for r in range(200, 400, 5):
   fp = sum([(ratio >= r/100.0) for ratio in normal_ratios]) / float(len(normal_ratios))
   fn = sum([(ratio < r/100.0) for ratio in slide_changes_ratios]) / float(len(slide_changes_ratios))
   print r, fp, fn
  
