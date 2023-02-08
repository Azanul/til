# How to install enumer
------------------------

Download
```bash
go get github.com/dmarkham/enumer
```

Sync vendor
```bash
go mod vendor
```

Install
```bash
go install github.com/dmarkham/enumer
```

Mark `.go` source files with
```go
//go:generate go run github.com/dmarkham/enumer -type=YOURTYPE
```

Run
```bash
go generate
```


ref: [dmarkham/enumer](https://github.com/dmarkham/enumer)
