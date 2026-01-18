import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Dashboard from "@/pages/Dashboard";
import CreateProduct from "@/pages/ProductCreate";
import Orders from "@/pages/Orders";
import Order from "@/pages/Order";
import Success from "@/pages/Success";


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/create-product" element={<CreateProduct />} />
        <Route path="/orders" element={<Orders />} />
        <Route path="/create-order" element={<Order />} />
        <Route path="/success" element={<Success />} />
      </Routes>
    </Router>
  );
};

export default App;