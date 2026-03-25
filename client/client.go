/*
Copyright © 2024 Lina Maria Fernandez Garcia
*/
package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net"
	"os"

	// "reflect"
	"strconv"
	// "reflect"
	// "strings"
)

type ProblemResults struct {
    Number int    `json:"number"`
    Result string `json:"result"`
}

type MyJson struct {
	Problem  string `json:"problem"`
	Quantity string `json:"Quantity"`
	Lower    string `json:"lower"`
	Upper    string `json:"upper"`
	Output   string `json:"Output"`
}

type MyJsonShutdown struct {
	Problem string `json:"problem"`
	Status  bool   `json:"status"`
}

func newMyJson(problem string, quantity string, lower string, upper string, output string) MyJson {
	my_json := MyJson{
		Problem:  problem,
		Quantity: quantity,
		Lower:    lower,
		Upper:    upper,
		Output:   output,
	}
	return my_json
}

type Client struct {
	data MyJson
	problem_results []byte
}

func (clientInstance Client) Generate_json() []byte {
	//fmt.Println("I'm Generate_json")
	my_json := clientInstance.data
	data_map := map[string]interface{}{
		"problem":  my_json.Problem,
		"quantity": my_json.Quantity,
		"lower":    my_json.Lower,
		"upper":    my_json.Upper,
		"output":   my_json.Output,
	}
	json_data, _ := json.Marshal(data_map)
	return json_data
}

func (clientInstance *Client) sockets_connection(message []byte) {

	//fmt.Println("I'm sockets_connection")
	fmt.Println("Sending request to problemSolver\n")

	const (
		SERVER_HOST = "localhost"
		SERVER_PORT = "8000"
		SERVER_TYPE = "tcp"
	)

	connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		panic(err)
	}
	_, err = connection.Write(message)
	if err != nil {
		fmt.Println("Error writing: ", err.Error())
		return
	}
	var fullMessage []byte
    buffer := make([]byte, 4096) 

    for {
        mLen, err := connection.Read(buffer)
        if err != nil {
            if err == io.EOF {
                break
            }
            fmt.Println("Error reading: ", err.Error())
            return
        }
        fullMessage = append(fullMessage, buffer[:mLen]...)
        if mLen < len(buffer) {
            break
        }
    }
	defer connection.Close() 
	if len(fullMessage) == 27 {
		fmt.Println("Received: ", string(fullMessage))
	} else {
		fmt.Println("Response to solution received\n")
	}
	clientInstance.problem_results = fullMessage
}

func (clientInstance Client) shutdown() {
	//fmt.Println("I'm shutdown")
	fmt.Println("Shutting down system\n")
	
		my_json := MyJsonShutdown{
			Problem: "shutdown",
			Status:  false,
		}
		data_map := map[string]interface{}{
			"problem": my_json.Problem,
			"status":  my_json.Status,
		}
		json_data, _ := json.Marshal(data_map)
		clientInstance.sockets_connection(json_data)
}

// Get password from file and compare with the input
func (clientInstance Client) authentication(password_client string) bool {
	// fmt.Println("I'm authentication")
	fmt.Println("Authenticating password\n")
	password := clientInstance.read_data("config.txt")
	return password[0] == password_client
}

//converts the information in json format to an array of strings
func (clientInstance Client) convert_json_to_array() []ProblemResults{
	//fmt.Println("I'm convert_json_to_array")
	aux := clientInstance.problem_results

	var results []ProblemResults
	err := json.Unmarshal(aux, &results)

    if err != nil {
        log.Fatal(err)
    }
	return results
}

// Create a txt file to write the results from ProblemSolver
func (clientInstance Client) save__data() {

	//fmt.Println("I'm save_data")
	fmt.Println("Saving Data\n")
	f, err := os.Create("data.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	problem_results := clientInstance.convert_json_to_array()

	for i := 0; i < len(problem_results); i++ {
		result := problem_results[i]
		result_str := strconv.Itoa(result.Number) + " " + result.Result
		l, err := f.WriteString(result_str+ "\n")
		_ = l
		if err != nil {
			fmt.Println(err)
			f.Close()
			return
		}
	}
}

// read the file to return a strings array with the data
func (clientInstance Client) read_data(file_name string) []string {
	file_data := []string{}
	file, err := os.Open(file_name)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		file_data = append(file_data, line)
	}
	return file_data
}

// Read data from the file to print it in console
func (clientInstance Client) print_data(){
	data := clientInstance.read_data("data.txt")
	for i := 0; i < len(data); i++ {
		fmt.Println(data[i])
	}
}
