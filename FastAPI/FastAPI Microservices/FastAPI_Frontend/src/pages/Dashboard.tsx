import Layout from "./Layout"
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { CirclePlus } from "lucide-react"
import { Separator } from "@/components/ui/separator"
import axios from "axios";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom"


function Dashboard() {
    const [data, setData] = useState<any[]>([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get("http://localhost:8000/products/");
                setData(response.data);
            } catch (error) {
                console.log(error);
            }
        };
        fetchData();
    }, []);
    console.log(data)

    const handleDelete = async (id: string) => {
        if (window.confirm("Are you sure you want to delete this product?")) {
            try {
                await axios.delete(`http://localhost:8000/products/${id}`);
                setData(data.filter((product) => product.id !== id));
            } catch (error) {
                console.log(error);
                setData(data.filter((product) => product.id !== id))
            }
        }

    }



    return (
        <Layout>
            <div className="p-4 md:p-6 lg:p-8 w-full mx-auto">
                <div className="flex flex-row">
                    <h1 className="text-2xl font-semibold mb-4">Dashboard</h1>
                    <Link to="/create-product" className="ml-auto">
                        <Button variant="outline">
                            <CirclePlus /> Quick Create
                        </Button>
                    </Link>
                </div>

                <Separator className="my-2" />

                <Table>
                    <TableCaption>A list of your all products.</TableCaption>
                    <TableHeader>
                        <TableRow>
                            <TableHead>Id</TableHead>
                            <TableHead>Name</TableHead>
                            <TableHead>Price</TableHead>
                            <TableHead>Quantity</TableHead>
                            <TableHead className="text-right">Action</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {data.map((product) => (
                            <TableRow key={product.id}>
                                <TableCell className="font-medium">{product.id}</TableCell>
                                <TableCell>{product.name}</TableCell>
                                <TableCell>{product.price}</TableCell>
                                <TableCell>{product.quantity}</TableCell>
                                <TableCell className="text-right">
                                    <button className="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded" onClick={() => handleDelete(product.id)}>
                                        Delete
                                    </button>
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </div>
        </Layout>
    )
}

export default Dashboard