import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;

import '../core/config.dart';
import '../models/models.dart';

class ApiService {
  final String _base = AppConfig.apiBaseUrl;

  Future<ChatReply> askBhoomi(String question) async {
    final res = await http.post(
      Uri.parse('$_base/bhoomi-chat'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'question': question, 'language': 'en'}),
    );
    return ChatReply.fromJson(jsonDecode(res.body));
  }

  Future<Map<String, dynamic>> weather(double lat, double lon) async {
    final res = await http.get(Uri.parse('$_base/weather?lat=$lat&lon=$lon'));
    return jsonDecode(res.body);
  }

  Future<List<MarketPrice>> marketPrices(String crop) async {
    final res = await http.get(Uri.parse('$_base/market-prices?crop=$crop'));
    return (jsonDecode(res.body) as List<dynamic>)
        .map((e) => MarketPrice.fromJson(e as Map<String, dynamic>))
        .toList();
  }

  Future<Map<String, dynamic>> diagnosePlant(File imageFile) async {
    final request = http.MultipartRequest('POST', Uri.parse('$_base/plant-diagnosis'));
    request.files.add(await http.MultipartFile.fromPath('file', imageFile.path));
    final response = await request.send();
    final body = await response.stream.bytesToString();
    return jsonDecode(body);
  }
}
