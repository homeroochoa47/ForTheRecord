// webpack.config.js example
const path = require('path');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');
const {WebpackManifestPlugin} = require('webpack-manifest-plugin');
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js",
  plugins: [
    new WebpackManifestPlugin(), 
    new CleanWebpackPlugin(),  
  ],
  output: {
    path: path.resolve(__dirname, "./static/frontend"), // Should be in STATICFILES_DIRS
    publicPath: '',
    filename: "[name].js", // No filename hashing, Django takes care of this
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  }
}