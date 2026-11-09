import java.util.HashMap;
import java.util.List;
import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Path;

public class Builder{

    HashMap<List<String>, HashMap<String, Integer>> build(Path filepath, int order){
        HashMap<List<String>, HashMap<String, Integer>> backing = new HashMap<>();

        try(BufferedReader br = new BufferedReader(Files.newBufferedReader(filepath))){

            int count = 0;
            String line = "";
            String[] prevWords = new String[order];
            while((line = br.readLine()) != null){
                String[] words = line.split("\\s+");

                for(String word: words){
                    if(count < order){
                        prevWords[count] = word;
                        count++;
                        continue;
                    }

                    backing.computeIfAbsent(List.of(prevWords), k -> new HashMap<>()).merge(word, 1, Integer::sum);

                    for(int i = 0; i < order-1; i++){
                        prevWords[i] = prevWords[i+1];
                    }
                    prevWords[order-1] = word;

                }
            }
        }catch(Exception e){
            System.out.println("Exception Caught: " + e);
        }

        return backing;
    }



}