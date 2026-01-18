import Navbar from "@/components/Navbar";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { useForm } from "react-hook-form";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { Separator } from "@/components/ui/separator";
import { ThemeProvider } from "@/components/ThemeProvider";
import { useEffect, useState } from "react";

type OrderFormValues = {
  productId: string;
  quantity: number;
};

function Order() {
  const [message, setMessage] = useState("Buy your favorite product");
  const navigate = useNavigate();

  const form = useForm<OrderFormValues>({
    defaultValues: {
      productId: "",
      quantity: 1,
    },
  });

  const productId = form.watch("productId");
  const quantity = form.watch("quantity");

  useEffect(() => {
    async function getPrice() {
      if (!productId) {
        setMessage("Buy your favorite product");
        return;
      }

      try {
        const response = await axios.get(
          `http://localhost:8000/products/${productId}`
        );

        const price = response.data.price;
        const totalPrice = (price * 1.2) * quantity;

        setMessage(`Your product price is $${totalPrice.toFixed(2)}`);
      } catch (error) {
        console.log(error);
        setMessage("Buy your favorite product");
      }
    }

    getPrice();
  }, [productId, quantity]);

  async function onSubmit(data: OrderFormValues) {
    console.log("Order Data:", data);

    const orderData = {
      product_id: data.productId,
      quantity: data.quantity,
    };

    // Example: sending order to backend
    try {
      const response = await axios.post("http://127.0.0.1:8001/orders/", orderData);
      console.log(response.data);

      navigate("/success");
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <>
      <ThemeProvider defaultTheme="system" storageKey="vite-ui-theme">
        <Navbar />

        <div className="p-4 md:p-6 lg:p-8 w-full mx-auto mt-16 text-center">
          <h1 className="text-2xl font-semibold mb-4">Checkout Form</h1>
          <p>{message}</p>
          <Separator className="my-2 w-[80%] mx-auto" />
        </div>

        <div className="w-[80%] mx-auto">
          <Form {...form}>
            <form
              onSubmit={form.handleSubmit(onSubmit)}
              className="space-y-8"
            >
              <div className="flex flex-row gap-8">
                <FormField
                  control={form.control}
                  name="productId"
                  render={({ field }) => (
                    <FormItem className="w-[50%]">
                      <FormLabel>Product Id</FormLabel>
                      <FormControl>
                        <Input
                          placeholder="Give The Product Id Here"
                          {...field}
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />

                <FormField
                  control={form.control}
                  name="quantity"
                  render={({ field }) => (
                    <FormItem className="w-[50%] text-right">
                      <FormLabel>Quantity</FormLabel>
                      <FormControl>
                        <Input
                          type="number"
                          placeholder="How much Product do you want?"
                          {...field}
                          onChange={(e) =>
                            field.onChange(Number(e.target.value))
                          }
                        />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />
              </div>

              <Button className="w-full" type="submit">
                Submit
              </Button>
            </form>
          </Form>
        </div>
      </ThemeProvider>
    </>
  );
}

export default Order;
