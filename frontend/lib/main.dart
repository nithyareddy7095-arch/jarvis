import 'package:flutter/material.dart';

import 'screens/screens.dart';

void main() {
  runApp(const TravelWithFarmerApp());
}

class TravelWithFarmerApp extends StatelessWidget {
  const TravelWithFarmerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Travel with Farmer',
      theme: ThemeData(
        colorSchemeSeed: Colors.green,
        scaffoldBackgroundColor: const Color(0xFFF5FFF6),
        useMaterial3: true,
      ),
      initialRoute: '/',
      routes: {
        '/': (_) => const WelcomeScreen(),
        '/auth': (_) => const AuthScreen(),
        '/dashboard': (_) => const DashboardScreen(),
        '/chat': (_) => const BhoomiChatScreen(),
        '/scanner': (_) => const PlantScannerScreen(),
        '/weather': (_) => const WeatherScreen(),
        '/market': (_) => const MarketScreen(),
        '/learning': (_) => const LearningMarketplaceScreen(),
        '/community': (_) => const CommunityVideosScreen(),
        '/profile': (_) => const ProfileScreen(),
      },
    );
  }
}
