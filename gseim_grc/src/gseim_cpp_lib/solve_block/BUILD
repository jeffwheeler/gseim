cc_library(
    name = "params_db",
    srcs = [
        "param.cpp",
        "params_db.cpp",
    ],
    hdrs = [
        "param.h",
        "params_db.h",
    ],
    copts = ["-std=c++17"],
)

cc_test(
    name = "params_db_test",
    srcs = ["params_db_test.cpp"],
    deps = [
        ":params_db",
    ],
    copts = ["-std=c++17"],
)
