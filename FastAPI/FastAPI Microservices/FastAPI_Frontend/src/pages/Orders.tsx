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
import { Badge } from "@/components/ui/badge"


function Orders() {
    const [pk, setPk] = useState<any[]>([]);
    const [data, setData] = useState<any[]>([]);

    useEffect(() => {
        const fetchPK = async () => {
            try {
                const response = await axios.get("http://localhost:8001/orders/");
                setPk(response.data);
            } catch (error) {
                console.log(error);
            }
        };
        fetchPK();
    }, []);

    useEffect(() => {
        const fetchData = async () => {
            try {
                if (pk.length === 0) return;

                const requests = pk.map((order) =>
                    axios.get(`http://localhost:8001/order/${order}`)
                );

                const results = await Promise.all(requests);

                const ordersData = results.map(res => res.data);

                setData(ordersData);
            } catch (error) {
                console.log(error);
            }
        };

        fetchData();
    }, [pk]);

    console.log(data)



    return (
        <Layout>
            <div className="p-4 md:p-6 lg:p-8 w-full mx-auto">
                <div className="flex flex-row">
                    <h1 className="text-2xl font-semibold mb-4">Orders</h1>
                    <Link to="/create-order" className="ml-auto">
                        <Button variant="outline">
                            <CirclePlus /> Create Order
                        </Button>
                    </Link>
                </div>

                <Separator className="my-2" />

                <Table>
                    <TableCaption>A list of your all products.</TableCaption>
                    <TableHeader>
                        <TableRow>
                            <TableHead>PK</TableHead>
                            <TableHead>Product_Id</TableHead>
                            <TableHead>Price</TableHead>
                            <TableHead>Fee</TableHead>
                            <TableHead>Quantity</TableHead>
                            <TableHead>Total</TableHead>
                            <TableHead className="text-right">Status</TableHead>
                        </TableRow>
                    </TableHeader>
                    <TableBody>
                        {data.map((order) => (
                            <TableRow key={order.pk}>
                                <TableCell className="font-medium">{order.pk}</TableCell>
                                <TableCell>{order.product_id}</TableCell>
                                <TableCell>{order.price}</TableCell>
                                <TableCell>{order.fee}</TableCell>
                                <TableCell>{order.quantity}</TableCell>
                                <TableCell>{order.total * order.quantity}</TableCell>
                                <TableCell className="text-right">
                                    {order.status === "pending"
                                        ? <Badge variant="outline"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" className="tabler-icon tabler-icon-loader "><path d="M12 6l0 -3"></path><path d="M16.25 7.75l2.15 -2.15"></path><path d="M18 12l3 0"></path><path d="M16.25 16.25l2.15 2.15"></path><path d="M12 18l0 3"></path><path d="M7.75 16.25l-2.15 2.15"></path><path d="M6 12l-3 0"></path><path d="M7.75 7.75l-2.15 -2.15"></path></svg> {order.status}</Badge>
                                        : order.status === "completed"
                                            ? <Badge variant="outline"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" stroke="none" className="tabler-icon tabler-icon-circle-check-filled fill-green-500 dark:fill-green-400"><path d="M17 3.34a10 10 0 1 1 -14.995 8.984l-.005 -.324l.005 -.324a10 10 0 0 1 14.995 -8.336zm-1.293 5.953a1 1 0 0 0 -1.32 -.083l-.094 .083l-3.293 3.292l-1.293 -1.292l-.094 -.083a1 1 0 0 0 -1.403 1.403l.083 .094l2 2l.094 .083a1 1 0 0 0 1.226 0l.094 -.083l4 -4l.083 -.094a1 1 0 0 0 -.083 -1.32z"></path></svg> {order.status}</Badge>
                                            : <Badge variant="outline"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" stroke="none" className="tabler-icon tabler-icon-circle-x-filled fill-red-500 dark:fill-red-400">
                                                <path d="M17 3.34a10 10 0 1 1 -14.995 8.984l-.005 -.324l.005 -.324a10 10 0 0 1 14.995 -8.336zm-5 7.246l-2.293 -2.293a1 1 0 0 0 -1.414 1.414l2.293 2.293l-2.293 2.293a1 1 0 0 0 1.414 1.414l2.293 -2.293l2.293 2.293a1 1 0 0 0 1.414 -1.414l-2.293 -2.293l2.293 -2.293a1 1 0 0 0 -1.414 -1.414l-2.293 2.293z"></path>
                                            </svg>
                                                {order.status}</Badge>
                                    }
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
            </div>
        </Layout>
    )
}

export default Orders