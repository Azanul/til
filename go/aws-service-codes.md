# Get all aws service codes
-----------------------------

Import `"github.com/aws/aws-sdk-go-v2/service/pricing"` & use `pricing.New()` for creating pricingClient.
```go
x, _ := pricingClient.DescribeServices(ctx, &pricing.DescribeServicesInput{})
for {
  for _, y := range x.Services {
    fmt.Println(*y.ServiceCode)
  }
  if x.NextToken == nil {
    break
  }
  x, _ = pricingClient.DescribeServices(ctx, &pricing.DescribeServicesInput{NextToken: x.NextToken})
}
```
