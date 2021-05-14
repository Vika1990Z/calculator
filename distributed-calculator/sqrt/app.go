// ------------------------------------------------------------
// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.
// ------------------------------------------------------------

package main

import (
        "encoding/json"
    "log"
        "net/http"
        "fmt"
        "math"
        "github.com/gorilla/mux"
)

type Operands struct {
    OperandOne float64 `json:"operandOne,string"`

}


func sqrt(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Content-Type", "application/json")
        w.Header().Set("Access-Control-Allow-Origin", "*")
        var operands Operands
        json.NewDecoder(r.Body).Decode(&operands)
        fmt.Println(fmt.Sprintf("%s%s%f", "Square root", " of ", operands.OperandOne))
        json.NewEncoder(w).Encode(math.Sqrt(operands.OperandOne))

}

func main() {
        router := mux.NewRouter()

        router.HandleFunc("/sqrt", sqrt).Methods("POST", "OPTIONS")
        log.Fatal(http.ListenAndServe(":9000", router))
}
