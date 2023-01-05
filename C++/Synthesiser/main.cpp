#include <iostream>
#include <math.h>

#include "olcNoiseMaker.h"

using namespace std;

atomic<double> dFrequencyOutput = 0.0;

double MakeNoise(double dTime){

    return 0.3*sin(dFrequencyOutput * 2 * 3.14159 * dTime) + 0.3*sin((dFrequencyOutput+20) * 2 * 3.14159 * dTime);
}

int main(){

    vector<wstring> devices = olcNoiseMaker<short>::Enumerate();

    for(auto d : devices) wcout << "Found Output Device" << d << endl;

    olcNoiseMaker<short> sound(devices[0], 44100, 1, 8, 512);

    sound.SetUserFunction(MakeNoise);

    double baseFreq = 220.0;
    double perSemitone = pow(2.0, 1.0/12.0);
    bool isPressed = false;

    while(1){

        isPressed = false;

        for(int i=0; i<15; i++)
            if(GetAsyncKeyState((unsigned char)("AWSEDFTGYHUJKOL"[i])) & 0x8000){
                dFrequencyOutput = baseFreq * pow(perSemitone, i);
                isPressed = true;
            }

        if(!isPressed)
            dFrequencyOutput = 0;
    }

    return 0;
}