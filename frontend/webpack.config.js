const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const FileManagerPlugin = require("filemanager-webpack-plugin");
const path = require("path");

const mode = process.env.NODE_ENV || "development";
const prod = mode === "production";

module.exports = {
    entry: {
        "build/bundle": ["./src/main.js"],
    },
    resolve: {
        alias: {
            svelte: path.dirname(require.resolve("svelte/package.json")),
        },
        extensions: [".mjs", ".js", ".svelte"],
        mainFields: ["svelte", "browser", "module", "main"],
    },
    output: {
        path: path.join(__dirname, "/public"),
        filename: "[name].js",
        chunkFilename: "[name].[id].js",
    },
    module: {
        rules: [
            {
                test: /\.svelte$/,
                use: {
                    loader: "svelte-loader",
                    options: {
                        compilerOptions: {
                            dev: !prod,
                        },
                        emitCss: prod,
                        hotReload: !prod,
                    },
                },
            },
            {
                test: /\.css$/,
                use: [MiniCssExtractPlugin.loader, "css-loader"],
            },
            {
                // required to prevent errors from Svelte on Webpack 5+
                test: /node_modules\/svelte\/.*\.mjs$/,
                resolve: {
                    fullySpecified: false,
                },
            },
        ],
    },
    mode,
    plugins: [
        new MiniCssExtractPlugin({
            filename: "[name].css",
        }),
        new FileManagerPlugin({
            events: {
                onEnd: [
                    {
                        copy: [
                            {
                                source: path.join(__dirname, "/public/build/*.js"),
                                destination: path.join(__dirname, "../public"),
                            },
                            {
                                source: path.join(__dirname, "/public/build/*.css"),
                                destination: path.join(__dirname, "../public"),
                            },
                        ],
                    },
                    // {
                    //     delete: [path.join(__dirname, "/public/build/")],
                    // },
                ],
            },
        }),
    ],
    devtool: prod ? false : "source-map",
    devServer: {
        hot: true,
        static: path.resolve(__dirname, "public"),
        proxy: {
            "/speak": "http://127.0.0.1:8000",
            "/get_audio_file": "http://127.0.0.1:8000",
        },
    },
};
