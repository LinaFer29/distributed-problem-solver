/*
Copyright © 2024 Lina Maria Fernandez Garcia
*/
package main

import (
	// "encoding/json"
	"fmt"
	"strings"
	// "test/finalProject2024I_TPA/client/cmd"
)

func shutdown_management(password string) {
	client := Client{
		data:            MyJson{},
		problem_results: []byte{},
	}
	var flag = client.authentication(password)
	if !flag{
		fmt.Println("Incorrect Password, try again")
	} else{
		client.shutdown()
	}
}

func run_client(dataCmd []string) {
	my_json := newMyJson(dataCmd[0], dataCmd[1], dataCmd[2], dataCmd[3], dataCmd[4])
	client := Client{
		data: my_json,
		problem_results: []byte{},
	}

	var dataJson = client.Generate_json()
	client.sockets_connection(dataJson)
	//client.convert_json_to_array()
	client.save__data()
	output := strings.ToLower(dataCmd[4])
	if output == "print"{
		fmt.Println("Printing results of the problem solver\n")
		client.print_data()
	} else {
		fmt.Println("The results of problemSolver have been saved, check the file!\n")
	}
	
}

func main() {
	fmt.Println("\n--------- PROBLEM SOLVER APPLICATION ---------\n")
	Execute()
}
