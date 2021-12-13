//
// Copyright (C) 2021 Storm Project.
//
// storm-reprozip-proxy is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

package parser

import (
	"encoding/json"
	"fmt"
	"os"
	path "path"

	decentcopy "github.com/storm-platform/tp-go-decent-copy"
)

func LoadConfigurationFile(filename string) (Configuration, error) {

	var config Configuration

	configFile, err := os.Open(filename)
	// defer configFile.Close()

	if err != nil {
		return config, err
	}

	jsonParser := json.NewDecoder(configFile)
	err = jsonParser.Decode(&config)

	return config, err
}

func Parser(operationType string, executionId string, config Configuration) {

	// Selecting the file type
	var files []FileDefinition

	if operationType == "input" {
		files = config.Inputs
	} else {
		files = config.Outputs
	}

	// Copying the files
	fmt.Println("Copying the files")
	for i := 0; i < len(files); i++ {
		if files[i].ExecutionId == executionId {
			// Creating the directory
			os.MkdirAll(path.Dir(files[i].Target), 0755)

			// Copy!
			err := decentcopy.Copy(files[i].Source, files[i].Target)

			if err != nil {
				fmt.Printf("Error in copy file : %#v ", err.Error())
			}
		}
	}

}
