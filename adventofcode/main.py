#!/usr/bin/env/ python3

from pathlib import Path


def _count_increases(in_list):
    return sum(in_list[idx + 1] - in_list[idx] > 0 for idx in range(len(in_list) - 1))


def _load_text(in_file):
    in_file = Path(in_file)

    with in_file.open("r") as FID:
        data = FID.readlines()
    return data


def _convert_to_float(in_list):
    if isinstance(in_list[0], str):
        return [float(idx) for idx in in_list]

    return in_list


def _sum_over_sliding_window(in_list, step_size=1):
    return [
        sum(in_list[idx : idx + 3]) for idx in range(0, len(in_list) - 2, step_size)
    ]


def _read_position(in_str):
    spl_str = in_str.split(" ")
    spl_str[1] = float(spl_str[1])
    return spl_str


def _update_position(command, position):
    if command[0].lower() == "forward":
        position[0] += command[1]
        position[1] += command[1] * position[2]
    elif command[0].lower() == "down":
        position[2] += command[1]
    elif command[0].lower() == "up":
        position[2] -= command[1]

    return position


def find_final_position(instructions_path, position=[0, 0,0]):
    sub_instructions = _load_text(instructions_path)
    
    for line in sub_instructions:
        command = _read_position(line)
        
        position = _update_position(command,position)

    return position
