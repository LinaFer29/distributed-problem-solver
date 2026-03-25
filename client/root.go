/*
Copyright © 2024 Lina Maria Fernandez Garcia
*/
package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
	"unicode"

	// "reflect"
	// "test/finalProject2024I_TPA/client/mainCli"
	// "test/client/client"
	"github.com/spf13/cobra"
	// "finalProject2024I_TPA/main"
)

func isInt(string_list []string) bool {
	for i := 0; i < len(string_list); i++{
		number := string_list[i]
		for _, c := range number {
			if !unicode.IsDigit(c) {
				return false
			}
		}
	}
    return true
}

// rootCmd represents the base command when called without any subcommands

var rootCmd = &cobra.Command{
	Use:   "client",
	Short: "Application to solve three type of problems",
	Long: `Problem Solver application is a system where we can select a available problem, 
giving it data like the number of numbers to process, the range, the output type
and the authentication information.`,
	// Uncomment the following line if your bare application
	// has an action associated with it:
	// Run: func(cmd *cobra.Command, args []string) { },
}

var cmdProblemSolver = &cobra.Command{
	Use: "problemSolver [problem quantity lowerlimit upperlimit output]",
	Short: "Process the information to management the solution",	
	Long: `problemSolver is for process the information entered about 
the type of problem you want to solve, the number of numbers,
the range and the type of output`,
	Args: cobra.MaximumNArgs(5),
	Run: func(cmd *cobra.Command, args []string) {
		problems := []string{"fizzbuzz","fibonacciverifier","primeclassifier"}
		outputs := []string{"save","print"}
		valid_problem := slices.Contains(problems,strings.ToLower(args[0]))
		valid_output := slices.Contains(outputs,strings.ToLower(args[4]))
		valid_limits := args[2] < args[3]

		strings_numbers := []string{args[1],args[2],args[3]}

		valid_number := isInt(strings_numbers)

		if len(args) == 5 && valid_problem && valid_output && valid_limits && valid_number {
			run_client(args)
		} else {
			if !valid_problem {
				fmt.Println("Error: The first argument is not a valid problem")
				fmt.Println("This are the valid problems to solve : ", problems)
			}
			if !valid_output {
				fmt.Println("Error: The last argument is not a valid output")
				fmt.Println("This are the valid output type to generate: ", outputs)
			}
			if len(args) != 5 {
				fmt.Println("Error:  Exactly 5 arguments are required")
			}
			if !valid_limits {
				fmt.Println("Error:  lower limit must be greater than upper limit")
			}
			if !valid_number {
				fmt.Println("Error:   quantity/lower/upper must be a number")
			}
		}
	},
}


var cmdShutdown = &cobra.Command{
	Use: "shutdown [password]",
	Short: "Allows you to request shutdown of the entire system",	
	Long: `shutdown is a command that requires an argument to validate 
	that you are authorized to perform the system shutdown process. `,
	Args: cobra.MaximumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		shutdown_management(args[0])
		//Generate_json(args)
		// fmt.Println("type: " , reflect.TypeOf(args))
	},
}

// Execute adds all child commands to the root command and sets flags appropriately.
// This is called by main.main(). It only needs to happen once to the rootCmd.
func Execute() {
	rootCmd.AddCommand(cmdProblemSolver)
	rootCmd.AddCommand(cmdShutdown)
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {
	// Here you will define your flags and configuration settings.
	// Cobra supports persistent flags, which, if defined here,
	// will be global for your application.

	// rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.client.yaml)")

	// Cobra also supports local flags, which will only run
	// when this action is called directly.
	rootCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}


