package main

import (
    "archive/zip"
    "fmt"
    "io"
    "os"
    "path/filepath"
    "strings"
)

func main() {
    // Get the current working directory
    currentDir, err := os.Getwd()
    if err != nil {
        fmt.Println("Error getting current directory:", err)
        return
    }

    // Create a new zip file
    zipFileName := "Prob_folders.zip"
    zipFile, err := os.Create(zipFileName)
    if err != nil {
        fmt.Println("Error creating zip file:", err)
        return
    }
    defer zipFile.Close()

    // Create a new zip archive
    zipWriter := zip.NewWriter(zipFile)
    defer zipWriter.Close()

    // Walk through the directory and its subdirectories
    err = filepath.Walk(currentDir, func(path string, info os.FileInfo, err error) error {
        if err != nil {
            return err
        }

        // If the file is a directory and its name starts with "Prob_"
        if info.IsDir() && strings.HasPrefix(info.Name(), "Prob_") {
            // Create a new zip file for the directory
            zipDirName := info.Name() + ".zip"
            zipDir, err := zipWriter.Create(zipDirName)
            if err != nil {
                return err
            }

            // Open the directory and its contents
            dir, err := os.Open(path)
            if err != nil {
                return err
            }
            defer dir.Close()

            // Get a list of all files and folders in the directory
            files, err := dir.Readdir(0)
            if err != nil {
                return err
            }

            // Add each file and folder to the zip file
            for _, file := range files {
                filePath := filepath.Join(path, file.Name())
                if file.IsDir() {
                    // If the file is a directory, add it recursively
                    err = zipDirectory(zipWriter, filePath, zipDirName)
                    if err != nil {
                        return err
                    }
                } else {
                    // If the file is a regular file, add it to the zip file
                    file, err := os.Open(filePath)
                    if err != nil {
                        return err
                    }
                    defer file.Close()

                    // Create a new zip file for the regular file
                    zipFileName := file.Name()
                    zipFile, err := zipWriter.Create(zipFileName)
                    if err != nil {
                        return err
                    }

                    // Copy the contents of the file to the zip file
                    _, err = io.Copy(zipFile, file)
                    if err != nil {
                        return err
                    }
                }
            }
        }

        return nil
    })
    if err != nil {
        fmt.Println("Error walking through directory:", err)
        return
    }

    fmt.Println("Successfully created zip file:", zipFileName)
}

func zipDirectory(zipWriter *zip.Writer, path string, parent string) error {
    // Create a new zip file for the directory
    zipDirName := filepath.Join(parent, filepath.Base(path)+".zip")
    zipDir, err := zipWriter.Create(zipDirName)
    if err != nil {
        return err
    }

    // Open the directory and its contents
    dir, err := os.Open(path)
    if err != nil {
        return err
    }
    defer dir.Close()

    // Get a list of all files and folders in the directory
    files, err := dir.Readdir(0)
    if err != nil {
        return err
    }

    // Add each file and

