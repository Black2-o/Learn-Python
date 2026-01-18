import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/Sidebar"
import Navbar from "@/components/Navbar"
import { ThemeProvider } from "@/components/ThemeProvider"


export default function Layout({ children }: { children: React.ReactNode }) {
    return (
        <SidebarProvider>
            <AppSidebar />
            <main className="w-full">
                <div className="flex flex-1 mt-16">
                    <SidebarTrigger />
                    <ThemeProvider defaultTheme="system" storageKey="vite-ui-theme">
                        <Navbar />
                        {children}
                    </ThemeProvider>
                </div>
            </main>
        </SidebarProvider>
    )
}