#include <iostream>
#include <string>

using namespace std;

//======================
// Lớp cơ sở
//======================
class MediaFile {
public:
    virtual void play() {
        cout << "Playing media file..." << endl;
    }

    virtual string getType() {
        return "Media";
    }

    virtual ~MediaFile() {}
};

//======================
// AudioFile
//======================
class AudioFile : public MediaFile {
public:
    void play() override {
        cout << "Playing audio..." << endl;
    }

    string getType() override {
        return "Audio";
    }
};

//======================
// VideoFile
//======================
class VideoFile : public MediaFile {
public:
    void play() override {
        cout << "Rendering video..." << endl;
    }

    string getType() override {
        return "Video";
    }
};

//======================
// GameFile
//======================
class GameFile : public MediaFile {
public:
    void play() override {
        cout << "Launching 3D engine..." << endl;
    }

    string getType() override {
        return "Game";
    }
};

//======================
// Hàm đa hình
//======================
void openFile(MediaFile* file) {
    cout << "Loai tep: " << file->getType() << endl;
    file->play();
    cout << "------------------------" << endl;
}

//======================
// Main
//======================
int main() {

    MediaFile* files[3];

    files[0] = new AudioFile();
    files[1] = new VideoFile();
    files[2] = new GameFile();

    cout << "===== DANH SACH MEDIA =====" << endl;

    for (int i = 0; i < 3; i++) {
        openFile(files[i]);
    }

    for (int i = 0; i < 3; i++) {
        delete files[i];
    }

    return 0;
}