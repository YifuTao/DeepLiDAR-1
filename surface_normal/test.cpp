#include <iostream>
#include "clean.hpp"
#include "tool.h"

int main(){
	std::ifstream file("/home/yifu/workspace/DeepLiDAR_cyshih704/DeepLiDAR/path.txt");
	std:string INPUT_FILE, OUTPUT_FILE,cam;
	float intrinsics[3];
	while (std::getline(file, INPUT_FILE))
	{
		std::getline(file,OUTPUT_FILE);
		std::getline(file,cam);
		intrinsics[0] = std::stof(cam);
		std::getline(file,cam);
		intrinsics[1] = std::stof(cam);
		std::getline(file,cam);
		intrinsics[2] = std::stof(cam);
		get_normal(INPUT_FILE,OUTPUT_FILE,intrinsics);
		cout << OUTPUT_FILE << endl;
	}

}
