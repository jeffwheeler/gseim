#ifndef PARAMS_DB_H
#define PARAMS_DB_H

#include <map>
#include <string>

using namespace std;

class ParamsDb {
    public:
        ParamsDb();
    private:
        map<string, string> params;
};

ParamsDb PARAM_DB;

#endif
