//
// Copyright (C) 2021 Storm Project.
//
// storm-reprozip-proxy is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

package parser

type FileDefinition struct {
	Source      string `json:"source"`
	Target      string `json:"target"`
	ExecutionId string `json:"executionId"`
	Type        string `json:"type"`
}

type Configuration struct {
	Inputs  []FileDefinition `json:"inputs"`
	Outputs []FileDefinition `json:"outputs"`
}
