#include <iostream>
using namespace std;

class Artist
{
protected:
    int creativity;

public:
    Artist(int c)
    {
        creativity = c;
    }

    void draw()
    {
        cout << "Drawing..." << endl;
    }

    void work()
    {
        cout << "Artist working" << endl;
    }
};

class Coder
{
protected:
    int logic;

public:
    Coder(int l)
    {
        logic = l;
    }

    void code()
    {
        cout << "Coding..." << endl;
    }

    void work()
    {
        cout << "Coder working" << endl;
    }
};

class GameDev : public Artist, public Coder
{
public:
    GameDev(int c, int l)
        : Artist(c), Coder(l)
    {
    }

    void develop()
    {
        draw();
        code();
        cout << "Developing game..." << endl;
    }
};

int main()
{
    GameDev g(90, 95);

    g.draw();
    g.code();
    g.develop();

    cout << endl;

    g.Artist::work();
    g.Coder::work();

    return 0;
}