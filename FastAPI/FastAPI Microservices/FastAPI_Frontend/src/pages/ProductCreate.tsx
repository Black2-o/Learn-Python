import Layout from "./Layout"
import { Separator } from "@/components/ui/separator"
import { Button } from "@/components/ui/button"
import {
    Form,
    FormControl,
    // FormDescription,
    FormField,
    FormItem,
    FormLabel,
    FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { useForm } from "react-hook-form"
import { z } from "zod"
import { zodResolver } from "@hookform/resolvers/zod"
import axios from "axios"
import { useNavigate } from "react-router-dom"

const formSchema = z.object({
    name: z.string().min(2, {
        message: "Must be an Valid Product Name.",
    }),
    price: z.string().min(1, {
        message: "Must have a price.",
    }),
    quantity: z.string().min(1, {
        message: "Must have a quantity.",
    }),
})


function CreateProduct() {
    const navigate = useNavigate();
    const form = useForm<z.infer<typeof formSchema>>({
        resolver: zodResolver(formSchema),
        defaultValues: {
            name: "",
            price: "",
            quantity: ""
        }
    });
    async function onSubmit(newProduct: any) {
        console.log(newProduct);
        try {
            await axios.post("http://localhost:8000/products/", {
                name: newProduct.name,
                price: parseFloat(newProduct.price),
                quantity: parseInt(newProduct.quantity)
            });
        } catch (error) {
            console.log(error);
            alert("Error creating product.");
        }
        navigate("/dashboard");

    }
    return (
        <Layout>
            <div className="p-4 md:p-6 lg:p-8 w-full mx-auto">
                <h1 className="text-2xl font-semibold mb-4">Create Product</h1>
                <Separator className="my-2" />
                <Form {...form}>
                    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
                        <FormField
                            name="name"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Name</FormLabel>
                                    <FormControl>
                                        <Input placeholder="Product Name Here" {...field} />
                                    </FormControl>
                                    {/* <FormDescription>
                                        This is your public display name.
                                    </FormDescription> */}
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        <FormField
                            name="price"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Price</FormLabel>
                                    <FormControl>
                                        <Input type="number" placeholder="Product Price Here" {...field} />
                                    </FormControl>
                                    {/* <FormDescription>
                                        This is your public display name.
                                    </FormDescription> */}
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        <FormField
                            name="quantity"
                            render={({ field }) => (
                                <FormItem>
                                    <FormLabel>Quantity</FormLabel>
                                    <FormControl>
                                        <Input type="number" placeholder="How much Product do you have?" {...field} />
                                    </FormControl>
                                    {/* <FormDescription>
                                        This is your public display name.
                                    </FormDescription> */}
                                    <FormMessage />
                                </FormItem>
                            )}
                        />
                        <Button type="submit">Submit</Button>
                    </form>
                </Form>
            </div>
        </Layout>
    );
}
export default CreateProduct;