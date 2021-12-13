//
// Copyright (C) 2021 Storm Project.
//
// storm-reprozip-proxy is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

package main

import (
	"fmt"
	"os"

	"github.com/storm-platform/storm-reprozip-proxy/parser"
)

func main() {
	fmt.Println("Starting...")
	argsWithoutProg := os.Args[1:]

	// Extract some arguments
	var executionId = argsWithoutProg[0]
	var operationType = argsWithoutProg[2]
	var configurationFilePath = argsWithoutProg[1]

	// Reading the parse configurations
	fmt.Println("Reading the configuration file...")
	var config, _ = parser.LoadConfigurationFile(configurationFilePath)

	// Parsing!
	fmt.Println("Parsing...")
	parser.Parser(operationType, executionId, config)
}
