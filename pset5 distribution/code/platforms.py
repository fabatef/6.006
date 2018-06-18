from collections import defaultdict
from collections import deque
import copy
import pickle
from globals import *  



# Suggested functions:
def create_configuration(current_step_tuple,pltf):

	on_ground = False
	score = current_step_tuple[1]
	this_step = current_step_tuple[0]
	character_box = get_character_box(this_step[0])
	nxt_pltfs = []
	new_pltf = this_step[2]
	old_pos = list(this_step[0])[:]
	new_v = list(this_step[1])[:]
	disp = new_v[:]
	for i, platform in enumerate(pltf):
		pltf_box = platform[0]
		pltf_score = platform[1]
		if boxes_intersect(pltf_box, get_bottom_of_box(character_box)):
			on_ground = True
			# set vy to zero and dy to be on the upper platform.
			new_v[1] = 0
			disp[1] = pltf_box[1] - this_step[0][1]
			# if pltform's not stepped on, increase score
			if i not in this_step[2]:
				score += pltf[i][1]
				visted_pltfs = [j for j in this_step[2]]
				visted_pltfs.append(i)
				new_pltf = frozenset(visted_pltfs)
		elif boxes_intersect(pltf_box, character_box):
			# check if there's collison
			return nxt_pltfs
	if on_ground:
		moves = ['left','right','up','none']
		for move in moves:
			next_vel = new_v[:]
			next_disp = disp[:]
			if move == 'left':
				next_disp[0] -= 1
				next_vel[0] -= 1
			elif move == 'right':
				next_disp[0] += 1
				next_vel[0] += 1
			elif move == 'up':
				next_disp[1] = -3
				next_vel[1] = -3
			ntup = (((old_pos[0] + next_disp[0], old_pos[1] + next_disp[1]),tuple(clamp_speed(next_vel)),new_pltf),score,current_step_tuple[2]+1)
			nxt_pltfs.append(ntup)
	else: # do nothing (just gravity)
		
		new_v[1] += GRAVITY
		ntup = (((old_pos[0] + disp[0], old_pos[1] + disp[1]), tuple(clamp_speed(new_v)), new_pltf), score, current_step_tuple[2]+1)
		nxt_pltfs.append(ntup)
	return nxt_pltfs

def dp_platf(n):
        counter = n
        memo = deque()
        memo. add(0)
        while counter != 0:
                result+= memo.popleft()
        return result

# This is the function called in tests.py and the autograder.
def calculate_best_score(pltf):
	scores = {}
	max_score = 0
	time = 0
	pltf.append(INITIAL_PLATFORM)
	init_tuple = (((-200,200),(0,0),frozenset([])),0,0)
	queue = deque()
	queue.append(init_tuple)
	while queue:
		step_tuple = queue.popleft()
		if step_tuple[2] <= 600:
			this_step = step_tuple[0]
			score = step_tuple[1]
			if score > max_score:
				max_score = score
			if abs(this_step[0][0]) < 600 and abs(this_step[0][1]) < 600:
				if this_step not in scores:
					scores[this_step] = score
				nxt_pltfs = create_configuration(step_tuple,pltf)
				for nxt in nxt_pltfs:
					score = nxt[1]
					step = nxt[0]
					if step not in scores or (step in scores and scores[step]<score):
						queue.append(nxt)
						scores[step] = score
	return max_score
