import { Home, BadgePlus, ShoppingBasket, Settings } from "lucide-react"

import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarGroupContent,
  // SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/components/ui/sidebar"

// Menu items.
const items = [
  {
    title: "Home",
    url: "/dashboard",
    icon: Home,
  },
  {
    title: "Add Product",
    url: "/create-product",
    icon: BadgePlus,
  },
  {
    title: "Orders",
    url: "/orders",
    icon: ShoppingBasket,
  },
  {
    title: "Order Create",
    url: "/create-order",
    icon: Settings,
  },
]

export function AppSidebar() {
  return (
    <Sidebar className="mt-16">
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild>
                    <a href={item.url}>
                      <item.icon />
                      <span>{item.title}</span>
                    </a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  )
}