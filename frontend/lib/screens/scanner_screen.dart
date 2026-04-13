import 'dart:io';

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

import '../services/api_service.dart';

class PlantScannerScreen extends StatefulWidget {
  const PlantScannerScreen({super.key});

  @override
  State<PlantScannerScreen> createState() => _PlantScannerScreenState();
}

class _PlantScannerScreenState extends State<PlantScannerScreen> {
  final _picker = ImagePicker();
  final _api = ApiService();
  String _result = 'Upload a leaf image to scan for disease.';

  Future<void> _scan() async {
    final image = await _picker.pickImage(source: ImageSource.gallery);
    if (image == null) return;
    final result = await _api.diagnosePlant(File(image.path));
    setState(() => _result = 'Disease: ${result['disease_type']}\nConfidence: ${result['confidence']}\nRecommendation: ${result['recommendation']}');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Plant Disease Scanner')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            ElevatedButton(onPressed: _scan, child: const Text('Upload Leaf Image')),
            const SizedBox(height: 16),
            Text(_result),
          ],
        ),
      ),
    );
  }
}
