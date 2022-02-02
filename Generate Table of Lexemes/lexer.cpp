#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <regex>
#include <stdio.h>

#include <map>
#include <vector>

using namespace std;

string str;
string currentword;

char currentchar;
double size = str.length();

map<string, unsigned char> reservedwords;
map<string, vector<long>> words;

vector<string> typeenum (10, "");


void readFile(){
	string myString = "";
	// Read from the text file
	ifstream MyReadFile("sometext.spyc");
	
	// Use a while loop together with the getline() function to read the file line by line
	while (getline (MyReadFile, myString)) {
	// Output the text from the file
	//cout << str << "\n";
	str += myString + "\n";
	}
	cout << str;
	str.pop_back();
	size = str.length();
}
void setup(){
	vector<string> reserves = {"as", "assert", "break", "bool", "boolean", "char", "character", "class", "continue", "def", "define", "del", "delete", "otherwise", "except", "finally", "False", "for", "from", "global", "whenever", "import", "in", "int", "integer", "is", "lambda", "nonlocal", "None", "pass", "raise", "return", "True", "try", "with", "while"};
	vector<string> all_symbols = {"+", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "{", "}", "~", "[", "\\", "]", "^", "`"};
	vector<string> other_symbols = {",", ".", ";", "#", "/", "\\", "`", "\"", "!", "|", "<", ">", "(", ")", "%", "&", "^", "*", "-", "+", "[", "]", "{"};
	vector<string> relational_op = {"<", "<=", ">", "=>", "==", "!=", "&&"};
	vector<string> assignment_op = {"=", "+=", "-=", "*=", "/=", "%=", "//="};
	vector<string> arithmetic_op = {"+", "-", "*", "/", "//", "%", "^"};
	
	typeenum[0] = "undefined_type";
	for(auto itr:reserves){
		reservedwords[itr] = 1;
		typeenum[1] = "reserved_word";
	}
	for(auto itr:all_symbols){
		reservedwords[itr] = 2;
		typeenum[2] = "any_symbol";
	}
	for(auto itr:other_symbols){
		reservedwords[itr] = 3;
		typeenum[3] = "symbol";
	}
	for(auto itr:relational_op){
		reservedwords[itr] = 4;
		typeenum[4] = "relational_operator";
	}
	for(auto itr:assignment_op){
		reservedwords[itr] = 5;
		typeenum[5] = "assignment_operator";
	}
	for(auto itr:arithmetic_op){
		reservedwords[itr] = 6;
		typeenum[6] = "arithmetic_operator";
	}
}

unsigned int possible = 0;
void checkPossibles(char in1, char in2){			//Initial Check for Possible Types of next Word
	//1 Possible Number
}

bool isDigit(char in){
	return in > 47 && in < 58 ? true : false;
}
bool isAlpha(char in){
	return (in > 61 && in < 91) || (in > 96 && in < 123) ? true : false;
}
bool isSymbol(char in){
	string strin = "";
	strin += in;
	return reservedwords[strin] == 2 || reservedwords[strin] == 3 || reservedwords[strin] == 4 || reservedwords[strin] == 6 ? true : false;
}

int getType(char in){
	if(isDigit(in))return 1;
	else if(isAlpha(in))return 2;
	else if(isSymbol(in))return 3;
	//else return 3;
}

int lasttype = 0;
int startchartype = 0;

bool toPush = true;

int main(){
	setup();
	readFile();
	
	for(double i = 0; i < size; i++){
		currentchar = str.at(i);
		cout << currentchar;
		if(toPush){
			startchartype = getType(currentchar);
		}
		toPush = false;
		
		if(startchartype == 1){
			if((currentchar == ' ' || currentchar == '\n')){
				toPush = true;
			}
			else if(isDigit(currentchar)){
				currentword += currentchar;
			}
			else if(currentchar == '.'){
				currentword += currentchar;
			}
			else if(isAlpha(currentchar)){
				cout << "Error!";
				return 0;
			}
			else{
				toPush = true;
				i--;
			}
		}
		
		else if(startchartype == 2){
			if((currentchar == ' ' || currentchar == '\n')){
				toPush = true;
			}
			else if(isDigit(currentchar)){
				currentword += currentchar;
			}
			else if(isSymbol(currentchar)){
				toPush = true;
				i--;
			}
			else{
				currentword += currentchar;
			}
		}
		
		else if(startchartype == 3){
			if((currentchar == ' ' || currentchar == '\n')){
				toPush = true;
			}
			else if(isSymbol(currentchar)){
				currentword += currentchar;
			}
			else{
				toPush = true;
				i--;
			}
		}
		
		if(toPush){
			words[(string) currentword].push_back(i-currentword.length());
			//cout << "sct: " << startchartype << " Putting " << currentword << "\n";
			cout << currentword << " " << "\n";
			currentword = "";
		}
	}
	
	words[currentword].push_back(size-1-currentword.length());
	cout << currentword;
	
	std::ofstream out("out.csv");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	for (auto itr = words.begin(); itr != words.end(); ++itr){
		cout << itr->first << "," << typeenum[(int)reservedwords[itr->first]] << ",";
		for (auto ptr = itr->second.begin(); ptr != itr->second.end(); ptr++) {
			cout << *ptr << " " ;
		}
		cout << "\n";
	}
	
	std::cout.rdbuf(coutbuf); //reset to standard output againS
}
